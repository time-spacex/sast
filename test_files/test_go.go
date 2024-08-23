package main

import (
    "fmt"
    "net/http"
)

func vulnerableHandler(w http.ResponseWriter, r *http.Request) {
    // Path Traversal vulnerability
    file := r.URL.Query().Get("file")
    http.ServeFile(w, r, "/var/www/"+file)
}

func main() {
    http.HandleFunc("/", vulnerableHandler)
    fmt.Println("Server is listening...")
    http.ListenAndServe(":8080", nil)
}
