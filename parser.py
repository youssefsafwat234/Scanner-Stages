class GrammarCheckerApp:
    def _init_(self):
        self.production_rules = {'S': [], 'B': []}
        self.is_valid_grammar = False  # Indicates if the grammar is valid and simple

    def display_menu(self):
        print("\nOptions Menu:")
        print("1. Input Grammar Rules")
        print("2. Validate String Against Grammar")
        print("3. Quit Application")

    def input_grammar(self):
        print("\nProvide the production rules:")

        # Input rules for S
        rule_s1 = input("Enter the first rule for S: ").strip()
        rule_s2 = input("Enter the second rule for S: ").strip()

        # Input rules for B
        rule_b1 = input("Enter the first rule for B: ").strip()
        rule_b2 = input("Enter the second rule for B: ").strip()

        # Validate simplicity of grammar
        if self.validate_rules([rule_s1, rule_s2]) and self.validate_rules([rule_b1, rule_b2]):
            self.production_rules['S'] = [rule_s1, rule_s2]
            self.production_rules['B'] = [rule_b1, rule_b2]
            self.is_valid_grammar = True
            print("\nGrammar rules are valid and accepted!")
        else:
            self.is_valid_grammar = False
            print("\nInvalid or non-simple grammar. Please try again.")

    def validate_rules(self, rules_list):
        unique_terminals = set()
        for rule in rules_list:
            if not rule or rule == "":
                return False
            if not rule[0].islower():  # Rule must start with a terminal
                return False
            if rule[0] in unique_terminals:  # Terminal must not repeat
                return False
            unique_terminals.add(rule[0])
        return True

    def validate_string(self):
        if not self.is_valid_grammar:
            print("\nThe current grammar is invalid. Cannot validate strings!")
            return

        test_string = input("\nEnter a string to validate: ").strip()
        if not test_string:
            print("\nPlease provide a string for validation!")
            return

        # Parsing logic with parse tree construction
        pointer = [0]
        syntax_tree = []

        def parse_nonterminal_S():
            start_pos = pointer[0]
            for rule in self.production_rules['S']:
                pointer[0] = start_pos
                sub_tree = []
                if match_pattern(rule, sub_tree, 'S'):
                    syntax_tree.append(('S', rule, sub_tree))
                    return True
            return False

        def parse_nonterminal_B():
            start_pos = pointer[0]
            for rule in self.production_rules['B']:
                pointer[0] = start_pos
                sub_tree = []
                if match_pattern(rule, sub_tree, 'B'):
                    syntax_tree.append(('B', rule, sub_tree))
                    return True
            return False

        def match_pattern(rule, sub_tree, nonterminal):
            for char in rule:
                if char.islower():  # Check for terminal
                    if pointer[0] < len(test_string) and test_string[pointer[0]] == char:
                        sub_tree.append(char)  # Add terminal to sub-tree
                        pointer[0] += 1
                    else:
                        return False
                elif char == 'S':  # Non-terminal S
                    sub_tree.append(('S',))  # Append non-terminal to sub-tree
                    if not parse_nonterminal_S():
                        return False
                elif char == 'B':  # Non-terminal B
                    sub_tree.append(('B',))  # Append non-terminal to sub-tree
                    if not parse_nonterminal_B():
                        return False
            return True

        if parse_nonterminal_S() and pointer[0] == len(test_string):
            print("\nThe string is ACCEPTED!")
        else:
            print("\nThe string is REJECTED!")

    def quit_app(self):
        print("\nThank you for using the Grammar Checker App. Goodbye!")
        exit()

    def run_application(self):
        while True:
            self.display_menu()
            user_choice = input("\nEnter your selection: ").strip()

            if user_choice == "1":
                self.input_grammar()
            elif user_choice == "2":
                self.validate_string()
            elif user_choice == "3":
                self.quit_app()
            else:
                print("\nInvalid selection. Please choose a valid option.")

# Start the program
if __name__ == "__main__":
    app = GrammarCheckerApp()
    app.run_application()