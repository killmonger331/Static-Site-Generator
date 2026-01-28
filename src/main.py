from textnode import TextNode, TextType
import os
import shutil
from copystatic import copy_static
print("hello world")

def main():
    copy_static("static", "public")
    output = TextNode("Sample Text", TextType.TEXT, "http://example.com")
    print(output)    
if __name__ == "__main__":
    main()

main()



def copy_static(src: str, dst: str):
    """
    Recursively copy all contents from src to dst.
    Deletes dst first to ensure a clean copy.
    """
    if os.path.exists(dst):
        print(f"Removing existing directory: {dst}")
        shutil.rmtree(dst)

    os.mkdir(dst)

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
            print(f"Copied file: {src_path} -> {dst_path}")

        else:
            print(f"Entering directory: {src_path}")
            copy_static(src_path, dst_path)
