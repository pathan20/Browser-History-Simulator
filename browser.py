# ============================================================
# BROWSER HISTORY SIMULATOR
# Data Structure: Stack
# ============================================================


class BrowserHistory:

    def __init__(self, homepage):
        # Stack for previously visited pages
        self.back_stack = []

        # Stack for pages available through Forward
        self.forward_stack = []

        # Current webpage
        self.current_page = homepage

    # --------------------------------------------------------
    # Visit a new webpage
    # --------------------------------------------------------
    def visit(self, url):

        # Store current page in Back stack
        self.back_stack.append(self.current_page)

        # Move to new page
        self.current_page = url

        # When a new page is visited,
        # Forward history is cleared
        self.forward_stack.clear()

        print("\nOpened:", self.current_page)

    # --------------------------------------------------------
    # Go Back
    # --------------------------------------------------------
    def go_back(self):

        if not self.back_stack:
            print("\nNo previous page available.")
            return

        # Current page goes to Forward stack
        self.forward_stack.append(self.current_page)

        # Take the last page from Back stack
        self.current_page = self.back_stack.pop()

        print("\nMoved Back to:", self.current_page)

    # --------------------------------------------------------
    # Go Forward
    # --------------------------------------------------------
    def go_forward(self):

        if not self.forward_stack:
            print("\nNo forward page available.")
            return

        # Current page goes to Back stack
        self.back_stack.append(self.current_page)

        # Take the last page from Forward stack
        self.current_page = self.forward_stack.pop()

        print("\nMoved Forward to:", self.current_page)

    # --------------------------------------------------------
    # Display Current Page
    # --------------------------------------------------------
    def show_current_page(self):

        print("\nCurrent Page:")
        print(self.current_page)

    # --------------------------------------------------------
    # Display Complete History
    # --------------------------------------------------------
    def show_history(self):

        print("\n" + "=" * 60)
        print("                BROWSER HISTORY")
        print("=" * 60)

        print("\nBack Stack:")
        if self.back_stack:
            for page in self.back_stack:
                print("  ", page)
        else:
            print("   Empty")

        print("\nCurrent Page:")
        print("   ", self.current_page)

        print("\nForward Stack:")
        if self.forward_stack:
            for page in reversed(self.forward_stack):
                print("  ", page)
        else:
            print("   Empty")

        print("=" * 60)


# ============================================================
# Main Program
# ============================================================

def main():

    print("=" * 60)
    print("             BROWSER HISTORY SIMULATOR")
    print("=" * 60)

    homepage = input("Enter your homepage: ").strip()

    if not homepage:
        homepage = "https://www.google.com"

    browser = BrowserHistory(homepage)

    print("\nBrowser started!")
    print("Current Page:", browser.current_page)

    while True:

        print("\n" + "-" * 50)
        print("1. Visit New Website")
        print("2. Go Back")
        print("3. Go Forward")
        print("4. Show Current Page")
        print("5. Show Browser History")
        print("6. Exit")
        print("-" * 50)

        choice = input("Enter your choice: ").strip()

        # ----------------------------------------------------
        # Visit
        # ----------------------------------------------------
        if choice == "1":

            url = input("Enter website URL: ").strip()

            if url:
                browser.visit(url)
            else:
                print("\nURL cannot be empty.")

        # ----------------------------------------------------
        # Back
        # ----------------------------------------------------
        elif choice == "2":

            browser.go_back()

        # ----------------------------------------------------
        # Forward
        # ----------------------------------------------------
        elif choice == "3":

            browser.go_forward()

        # ----------------------------------------------------
        # Current Page
        # ----------------------------------------------------
        elif choice == "4":

            browser.show_current_page()

        # ----------------------------------------------------
        # History
        # ----------------------------------------------------
        elif choice == "5":

            browser.show_history()

        # ----------------------------------------------------
        # Exit
        # ----------------------------------------------------
        elif choice == "6":

            print("\nBrowser History Simulator closed.")
            print("Thank you!")
            break

        else:

            print("\nInvalid choice! Please select 1-6.")


# ============================================================
# Program Execution
# ============================================================

if __name__ == "__main__":
    main()