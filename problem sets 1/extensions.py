file_name = input("Enter your file name: ").lower().strip()

if file_name.endswith(".gif"):
    print("image/gif")
elif file_name.endswith (".jpg") or file_name.endswith(".jpeg"):
    print("image/jpeg")
elif file_name.endswith (".png"):
    print("image/png")
elif file_name.endswith (".pdf"):
    print("application/pdf")
elif file_name.endswith (".txt"):
    print("text/plain")

elif file_name.endswith (".zip"):
    print("application/zip. Note, Windows uploads .zip files with the non-standard MIME type application/x-zip-compressed")

else:
    print("application/octet-stream")