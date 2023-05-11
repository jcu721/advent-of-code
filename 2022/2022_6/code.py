def part_one():
    with open('input.txt', 'r') as input_file:
        code_input = input_file.readline()

    # code_input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    marker = "jpqm"
    correct_index = 7
    last_four = []
    for index, char in enumerate(code_input):
        # print(last_four)
        if len(last_four) == 4:
            last_four.pop()
        last_four.insert(0, char)
        # breakpoint()
        if len(set(last_four)) == 4:
            print("".join(last_four))
            print(f"index = {index+1}")
            break


def part_two():
    with open('input.txt', 'r') as input_file:
        code_input = input_file.readline()

    # code_input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    # marker = "jpqm"
    # correct_index = 19
    last_four = []
    for index, char in enumerate(code_input):
        # print(last_four)
        if len(last_four) == 14:
            last_four.pop()
        last_four.insert(0, char)
        # breakpoint()
        if len(set(last_four)) == 14:
            print("".join(last_four))
            print(f"index = {index+1}")
            break



if __name__ == "__main__":
    part_two()
