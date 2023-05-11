
class Directories():
    directories = {}

    def part_one(self):
        """Find all directories with size < 100000."""
        with open('input.txt', 'r') as input_file:
            code_input = input_file.readlines()

        directories = {'/': []}
        current_dir = '/'
        i = 0

        while i < len(code_input):
            # map directories to their ls output
            line = code_input[i]
            match line.split():
                case ['$', 'cd', '/']
                    current_dir = '/'
                case ['$', 'cd', '..']:
                    pass
                case ['$', 'cd', new_dir]:
                    current_dir = new_dir
                    if current_dir not in directories.keys():
                        directories[current_dir] = []
                    if current_dir in directories.keys():
                        print(f"possible duplicate? {current_dir}")
                case ['$', 'ls']:
                    pass
                case ["dir", new_dir]:
                    directories[current_dir].append(new_dir)
                case [size, file_name]:
                    directories[current_dir].append(int(size))
                case _:
                    # this shouldn't happen
                    breakpoint()
            i += 1

        print(f"directories = {directories}")
        self.directories = directories

        total_sizes_summed = 0
        for directory in directories:
            total_dir_size = self.calculate_total_size(directory)
            print(f"{directory}: {total_dir_size}")
            if total_dir_size < 100000:
                total_sizes_summed += total_dir_size

        print(total_sizes_summed)

    def calculate_total_size(self, directory):
        # print(f"calculate_total_size of {directory}")
        # breakpoint()
        if isinstance(directory, int):  # is a file
            # print(f"is a file, returning {directory}")
            return directory
        else:  # is a directory
            # print(f"is a directory, doing some recursion")
            # already calculated this directory
            if isinstance(self.directories[directory], int):
                return self.directories[directory]

            # else, do the recursion
            sum = 0
            for item in self.directories[directory]:
                sum += self.calculate_total_size(item)
            self.directories[directory] = sum
            return sum


if __name__ == "__main__":
    # import sys
    # sys.setrecursionlimit(10000)
    Directories().part_one()
