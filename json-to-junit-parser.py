import json
import xml.etree.ElementTree as ET
from xml.dom import minidom

def create_junit_xml(json_data):
    # Создаем корневой элемент testsuites
    testsuites = ET.Element("testsuites")
    
    # Создаем элемент testsuite
    testsuite = ET.SubElement(testsuites, "testsuite", {
        "name": "Semgrep Security Scan",
        "tests": str(len(json_data["results"])),
        "errors": str(sum(1 for result in json_data["results"] if result["extra"]["severity"].upper() == "ERROR")),
        "warnings": str(sum(1 for result in json_data["results"] if result["extra"]["severity"].upper() == "WARNING")),
        "failures": "0"
    })
    
    # Добавляем каждый результат как testcase
    for result in json_data["results"]:
        testcase = ET.SubElement(testsuite, "testcase", {
            "name": result["check_id"],
            "classname": result["path"],
            "file": result["path"],
            "line": str(result["start"]["line"]),
        })
        
        if result["extra"]["severity"].upper() == "ERROR":
            error = ET.SubElement(testcase, "error", {
                "message": result["extra"]["message"],
                "type": result["extra"]["severity"]
            })
            error.text = result["extra"]["message"]
        elif result["extra"]["severity"].upper() == "WARNING":
            warning = ET.SubElement(testcase, "warning", {
                "message": result["extra"]["message"],
                "type": result["extra"]["severity"]
            })
            warning.text = result["extra"]["message"]
    
    return testsuites

def write_junit_xml(testsuites, output_path):
    # Преобразуем дерево в строку
    rough_string = ET.tostring(testsuites, encoding="utf-8")
    # Используем minidom для добавления отступов и переносов строк
    reparsed = minidom.parseString(rough_string)
    pretty_xml = reparsed.toprettyxml(indent="  ")
    
    # Записываем форматированный XML в файл
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(pretty_xml)

if __name__ == "__main__":
    # input_json_path = "./sast-2/result.json"
    # output_xml_path = "./sast-2/result.xml".
    input_json_path = "./result.json"
    output_xml_path = "./result.xml"
    
    with open(input_json_path, "r") as f:
        json_data = json.load(f)
    
    testsuites = create_junit_xml(json_data)
    write_junit_xml(testsuites, output_xml_path)
    
    print(f"JUnit XML report generated at {output_xml_path}")
