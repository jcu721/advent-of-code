def part_one():
    with open('input.txt', 'r') as input_file:
        code_input = input_file.readlines()

    break_index = code_input.index('\n')
    boxes = code_input[:break_index]

    num_boxes = int(code_input[break_index - 1].strip()[-1])
    meta_boxes = [[] for i in range(0, num_boxes + 1)]
    instructions = code_input[break_index + 1:]

    # construct boxes
    for line in boxes:
        # box width is 3 chars
        print(line)
        index = 0
        for box_number in range(1, num_boxes + 1):
            # breakpoint()
            # print(f"box_number = {box_number}")
            # print(f"index = {index}")
            # print(f"line[index] = {line[index]}")
            if line[index] == '[':
                # start of a box
                meta_boxes[box_number].append(line[index + 1])
                # print(meta_boxes)
            index += 4

    for box_stack in meta_boxes:
        box_stack.reverse()
    print(meta_boxes)
    for line in instructions:
        _, num_to_move, _, starting_box, _, ending_box = line.split()
        for i in range(0, int(num_to_move)):
            meta_boxes[int(ending_box)].append(meta_boxes[int(starting_box)].pop())

    answer = []
    for box_stack in meta_boxes[1:]:
        answer.append(box_stack[-1])

    print(''.join(answer))


def part_two():
    with open('input.txt', 'r') as input_file:
        code_input = input_file.readlines()

    break_index = code_input.index('\n')
    boxes = code_input[:break_index]

    num_boxes = int(code_input[break_index - 1].strip()[-1])
    meta_boxes = [[] for i in range(0, num_boxes + 1)]
    instructions = code_input[break_index + 1:]

    # construct boxes
    for line in boxes:
        index = 0
        for box_number in range(1, num_boxes + 1):
            if line[index] == '[':
                # start of a box
                meta_boxes[box_number].append(line[index + 1])
            index += 4

    for box_stack in meta_boxes:
        box_stack.reverse()
    print(meta_boxes)
    for line in instructions:
        _, num_to_move, _, starting_box, _, ending_box = line.split()
        x = int(num_to_move) * -1
        print(line)
        print(meta_boxes[int(starting_box)][x:])
        to_append = meta_boxes[int(starting_box)][x:]
        for item in to_append:
            meta_boxes[int(ending_box)].append(item)
            meta_boxes[int(starting_box)].pop()
        print(f"new meta_boxes = {meta_boxes}")
    answer = []
    for box_stack in meta_boxes[1:]:
        answer.append(box_stack[-1])

    breakpoint()
    print(''.join(answer))


if __name__ == "__main__":
    part_two()
