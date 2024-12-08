class BrowserNavigation:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []

    def visit_page(self, page):
        if self.back_stack:
            self.forward_stack.clear()
        self.back_stack.append(page)
        print(f"Visited page: {page}")

    def back(self):
        if len(self.back_stack) > 1:
            current_page = self.back_stack.pop()
            self.forward_stack.append(current_page)
            print(f"Back to page: {self.back_stack[-1]}")
        else:
            print("No more pages to go back.")

    def forward(self):
        if self.forward_stack:
            page = self.forward_stack.pop()
            self.back_stack.append(page)
            print(f"Forward to page: {page}")
        else:
            print("No more pages to go forward.")

    def current_page(self):
        print(f"Current page: {self.back_stack[-1]}")

browser = BrowserNavigation()

browser.visit_page("Page 1")
browser.visit_page("Page 2")
browser.visit_page("Page 3")

browser.back()
browser.back()

browser.forward()

browser.current_page()
