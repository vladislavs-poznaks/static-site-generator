from textnode import TextNode, TextType

def main():
    node = TextNode("test", TextType.NORMAL, "www.example.com")

    print(node)

if __name__ == "__main__":
    main()
