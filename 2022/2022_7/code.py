
class Directories():
    directories = {}

    def part_one(self):
        """Find all directories with size < 100000."""
        with open('input.txt', 'r') as input_file:
            code_input = input_file.readlines()

        directories = {'/': []}
        path = '/'
        i = 0
        dir_stack = []
        while i < len(code_input):
            # map directories to their ls output
            line = code_input[i]
            match line.split():
                case ['$', 'cd', '/']:
                    dir_stack = ['/']
                case ['$', 'cd', '..']:
                    dir_stack.pop()
                case ['$', 'cd', new_dir]:
                    dir_stack.append(new_dir)
                    path = "/".join(dir_stack)
                    if path not in directories.keys():
                        directories[path] = []
                    if path in directories.keys():
                        print(f"possible duplicate? {new_dir}")
                case ['$', 'ls']:
                    pass
                case ["dir", new_dir]:
                    directories[path].append(f"{path}/{new_dir}")
                case [size, file_name]:
                    directories[path].append(int(size))
                case _:
                    # this shouldn't happen
                    breakpoint()
            i += 1

        # print(f"directories = {directories}")
        self.directories = directories

        total_sizes_summed = 0
        sizes = []
        for directory in directories:
            total_dir_size = self.calculate_total_size(directory)
            # print(f"{directory}: {total_dir_size}")
            directories[directory] = total_dir_size
            sizes.append(total_dir_size)
            if total_dir_size < 100000:
                total_sizes_summed += total_dir_size

        print(f"part_one: {total_sizes_summed}")
        
        # breakpoint()
        size_to_delete = directories['/'] - 40000000
        print(f"must be greater than {size_to_delete}")
        # sizes.sort()
        # print(sizes)
        closest = 70000000
        for directory in directories:
            if directories[directory] >= size_to_delete:
                if directories[directory] < closest:
                    closest = directories[directory]
        
        print(closest)
        # 26391313 is too high



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
