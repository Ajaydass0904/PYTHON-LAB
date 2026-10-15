class State:
    def __init__(self, version, theme, font_size, notifications):
        self.version = version
        self.theme = theme
        self.font_size = font_size
        self.notifications = notifications
        self.next = None


class StateHistory:
    def __init__(self):
        self.head = None

    def add_state(self, state):
        if self.head is None:
            self.head = state
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = state

    def display_states(self):
        if self.head is None:
            print("\nNo states available.")
            return

        current = self.head

        print("\n--- State History ---")

        while current:
            print(
                f"Version {current.version} | "
                f"Theme: {current.theme} | "
                f"Font: {current.font_size} | "
                f"Notifications: {current.notifications}"
            )
            current = current.next

    def search_state(self, version):
        current = self.head

        while current:
            if current.version == version:
                return current
            current = current.next

        return None

    def delete_state(self, version):
        current = self.head
        previous = None

        while current:
            if current.version == version:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return True

            previous = current
            current = current.next

        return False


class RollbackStack:
    def __init__(self):
        self.stack = []

    def push(self, state):
        self.stack.append(state)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None

    def display(self):
        if not self.stack:
            print("\nRollback history is empty.")
            return

        print("\n--- Rollback History ---")

        for state in reversed(self.stack):
            print(f"Version {state.version}")


history = StateHistory()
rollback = RollbackStack()

version = 1

while True:

    print("\n==============================")
    print(" APPLICATION STATE MANAGER")
    print("==============================")
    print("1. Create New State")
    print("2. View State History")
    print("3. Search State")
    print("4. Rollback")
    print("5. Delete State")
    print("6. View Rollback History")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        theme = input("Enter theme (Dark/Light): ")
        font_size = int(input("Enter font size: "))
        notifications = input("Notifications (ON/OFF): ")

        new_state = State(
            version,
            theme,
            font_size,
            notifications
        )

        history.add_state(new_state)
        rollback.push(new_state)

        print(f"\nState Version {version} created successfully.")

        version += 1

    elif choice == "2":

        history.display_states()

    elif choice == "3":

        v = int(input("Enter version to search: "))

        result = history.search_state(v)

        if result:
            print("\nState Found!")
            print(f"Version       : {result.version}")
            print(f"Theme         : {result.theme}")
            print(f"Font Size     : {result.font_size}")
            print(f"Notifications : {result.notifications}")
        else:
            print("\nState not found.")

    elif choice == "4":

        state = rollback.pop()

        if state:
            print("\nRollback successful!")
            print(f"Restored Version: {state.version}")
            print(f"Theme: {state.theme}")
            print(f"Font Size: {state.font_size}")
            print(f"Notifications: {state.notifications}")
        else:
            print("\nNothing to rollback.")

    elif choice == "5":

        v = int(input("Enter version to delete: "))

        if history.delete_state(v):
            print(f"\nVersion {v} deleted successfully.")
        else:
            print("\nVersion not found.")

    elif choice == "6":

        rollback.display()

    elif choice == "7":

        print("\nExiting Application State Manager...")
        break

    else:
        print("\nInvalid choice!")
