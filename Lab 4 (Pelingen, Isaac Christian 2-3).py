# Steps in creating a cheesecake using Linked Lists
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    # a. Remove at beginning
    def remove_beginning(self):
        if not self.head:
            return None  # empty list
        removed_data = self.head.data
        self.head = self.head.next  # move head to the next node
        return removed_data

    # b. Remove at end
    def remove_at_end(self):
        if not self.head:
            return None  # empty list

        # If there's only one node
        if not self.head.next:
            removed_data = self.head.data
            self.head = None
            return removed_data

        # Find the second-to-last node
        current = self.head
        while current.next.next:
            current = current.next

        removed_data = current.next.data
        current.next = None  # remove last node
        return removed_data

    # c. Remove specific data
    def remove_at(self, data):
        if not self.head:
            return None  # empty list

        # If the data is in the head node
        if self.head.data == data:
            removed_data = self.head.data
            self.head = self.head.next
            return removed_data

        # Search for the node to remove
        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        # If data not found
        if not current.next:
            return None

        # If data found
        removed_data = current.next.data
        current.next = current.next.next
        return removed_data


# Create a linked list for cheesecake steps
cheesecake_steps = LinkedList()
cheesecake_steps.append("1. Prepare the crust by mixing graham cracker crumbs, sugar, and melted butter.")
cheesecake_steps.append("2. Press the mixture into the bottom of a springform pan.")
cheesecake_steps.append("3. Preheat the oven to 325°F (163°C).")
cheesecake_steps.append("4. In a large bowl, beat the cream cheese until smooth.")
cheesecake_steps.append("5. Add sugar and beat until combined.")
cheesecake_steps.append("6. Add eggs one at a time, beating well after each addition.")
cheesecake_steps.append("7. Mix in sour cream, vanilla extract, and lemon juice.")
cheesecake_steps.append("8. Pour the filling over the crust in the springform pan.")
cheesecake_steps.append("9. Bake for 55-70 minutes or until the center is almost set.")
cheesecake_steps.append("10. Turn off the oven and let the cheesecake cool in the oven for 1 hour.")
cheesecake_steps.append("11. Remove from the oven and refrigerate for at least 4 hours or overnight.")

# --- Example usage ---
print("\nOriginal Steps:")
cheesecake_steps.display()

print("\nRemoved from beginning:")
print(cheesecake_steps.remove_beginning())

print("\nRemoved from end:")
print(cheesecake_steps.remove_at_end())

print("\nRemoved specific step (step 5):")
print(cheesecake_steps.remove_at("5. Add sugar and beat until combined."))

print("\nUpdated Steps:")
cheesecake_steps.display()
