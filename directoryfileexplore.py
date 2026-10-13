
# DIRECTORY FILE EXPLORER VISUALIZER



# Node Class

class Node:

    def __init__(self, name, is_file=False):

        self.name = name

        # True  -> File
        # False -> Folder
        self.is_file = is_file

        
        self.children = {}



# File Explorer Class

class FileExplorer:

    def __init__(self):

        # Root directory
        self.root = Node("Root")


    
    # Create Folder or File

    def create(self, path, is_file):

        # Remove extra spaces and split path
        parts = [
            part for part in path.strip("/").split("/")
            if part
        ]

        if not parts:
            return "Invalid path."

        current = self.root

        # Move through parent folders
        for part in parts[:-1]:

            if part not in current.children:

                # Automatically create missing folders
                current.children[part] = Node(part)

            current = current.children[part]

            # A file cannot contain another file/folder
            if current.is_file:
                return "Error: Cannot create inside a file."

        name = parts[-1]

        # Check if already exists
        if name in current.children:
            return "File or folder already exists."

        # Create new node
        current.children[name] = Node(
            name,
            is_file
        )

        return "Created successfully."


    
    # Find a File or Folder

    def find(self, path):

        parts = [
            part for part in path.strip("/").split("/")
            if part
        ]

        current = self.root

        for part in parts:

            if part not in current.children:
                return None

            current = current.children[part]

        return current


    
    # Delete File or Folder
    

    def delete(self, path):

        parts = [
            part for part in path.strip("/").split("/")
            if part
        ]

        if not parts:
            return "Root folder cannot be deleted."

        current = self.root

        # Find parent directory
        for part in parts[:-1]:

            if part not in current.children:
                return "Path not found."

            current = current.children[part]

        name = parts[-1]

        if name not in current.children:
            return "File or folder not found."

        # Delete node
        del current.children[name]

        return "Deleted successfully."



    # Display Directory Tree
    

    def display(self, node=None, level=0):

        # Start from root
        if node is None:
            node = self.root

        # Indentation
        indentation = "    " * level

        # File or folder symbol
        if node.is_file:
            symbol = "📄"
        else:
            symbol = "📁"

        print(
            indentation +
            symbol +
            " " +
            node.name
        )

        # Sort folders before files
        children = sorted(
            node.children.values(),
            key=lambda item: (item.is_file, item.name.lower())
        )

        # Recursively display children
        for child in children:

            self.display(
                child,
                level + 1
            )


    
    # Search File or Folder using DFS
    

    def search(
        self,
        name,
        node=None,
        current_path=""
    ):

        if node is None:
            node = self.root

        # Create current path
        if current_path:

            path = current_path + "/" + node.name

        else:

            path = node.name

        results = []

        # Check current node
        if node.name.lower() == name.lower():

            results.append(path)

        # Search children recursively
        for child in node.children.values():

            results.extend(
                self.search(
                    name,
                    child,
                    path
                )
            )

        return results


# Main Program

def main():

    explorer = FileExplorer()

    
    # Sample Directory Structure
    

    explorer.create(
        "/Documents",
        False
    )

    explorer.create(
        "/Documents/Resume.pdf",
        True
    )

    explorer.create(
        "/Documents/Project.docx",
        True
    )

    explorer.create(
        "/Documents/College",
        False
    )

    explorer.create(
        "/Documents/College/Notes.txt",
        True
    )

    explorer.create(
        "/Pictures",
        False
    )

    explorer.create(
        "/Pictures/Photo1.jpg",
        True
    )

    explorer.create(
        "/Pictures/Photo2.jpg",
        True
    )

    explorer.create(
        "/Downloads",
        False
    )

    explorer.create(
        "/Downloads/Python.zip",
        True
    )
    # Menu
    

    while True:

        print("\n")
        print("=" * 60)
        print("          DIRECTORY FILE EXPLORER")
        print("=" * 60)

        print("1. Create Folder")
        print("2. Create File")
        print("3. Delete File/Folder")
        print("4. Display Directory")
        print("5. Search File/Folder")
        print("6. Check Path")
        print("7. Exit")

        print("=" * 60)

        choice = input(
            "Enter your choice: "
        ).strip()


        
        # Create Folder
        

        if choice == "1":

            path = input(
                "Enter folder path: "
            ).strip()

            result = explorer.create(
                path,
                False
            )

            print("\n" + result)


        
        # Create File
        

        elif choice == "2":

            path = input(
                "Enter file path: "
            ).strip()

            result = explorer.create(
                path,
                True
            )

            print("\n" + result)


        
        # Delete
        

        elif choice == "3":

            path = input(
                "Enter path to delete: "
            ).strip()

            result = explorer.delete(
                path
            )

            print("\n" + result)


        # Display
        

        elif choice == "4":

            print("\n")
            print("DIRECTORY STRUCTURE")
            print("-" * 40)

            explorer.display()


        
        # Search
        

        elif choice == "5":

            name = input(
                "Enter file/folder name to search: "
            ).strip()

            results = explorer.search(
                name
            )

            print("\nSEARCH RESULTS")
            print("-" * 40)

            if results:

                for result in results:

                    print("Found:", result)

            else:

                print("File or folder")
        # Check Path
        

        elif choice == "6":

            path = input(
                "Enter path: "
            ).strip()

            result = explorer.find(
                path
            )

            if result:

                if result.is_file:

                    print(
                        "\nPath exists."
                        "\nType: File"
                    )

                else:

                    print(
                        "\nPath exists."
                        "\nType: Folder"
                    )

            else:

                print(
                    "\nPath does not exist."
                )

        # Exit
        

        elif choice == "7":

            print(
                "\nDirectory File Explorer closed."
            )

            print(
                "Thank you!"
            )

            break


        
        # Invalid Choice
    

        else:

            print(
                "\nInvalid choice!"
            )



# Program Execution

if __name__ == "__main__":

    main()