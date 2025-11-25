back_stack = []
forward_stack = []
current_page = None

while True:
    print("\n1. Visit New Page")
    print("2. Go Back")
    print("3. Go Forward")
    print("4. Show History")
    print("5. Exit")

    ch = input("Enter choice: ")

    # Visit a new page
    if ch == "1":
        page = input("Enter page name/URL: ")

        if current_page is not None:
            back_stack.append(current_page)

        current_page = page
        forward_stack.clear()

        print("Visited:", current_page)

    # Go Back
    elif ch == "2":
        if not back_stack:
            print("No pages to go back to.")
        else:
            forward_stack.append(current_page)
            current_page = back_stack.pop()
            print("Back to:", current_page)

    # Go Forward
    elif ch == "3":
        if not forward_stack:
            print("No pages to go forward to.")
        else:
            back_stack.append(current_page)
            current_page = forward_stack.pop()
            print("Forward to:", current_page)

    # Show History
    elif ch == "4":
        print("\n--- Browser History ---")
        print("Back Stack:", back_stack)
        print("Current Page:", current_page)
        print("Forward Stack:", forward_stack)
        print("------------------------")

    # Exit
    elif ch == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
