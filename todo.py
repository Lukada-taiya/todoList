to_do_list = []


def menu():
    menu_list = '\n1. Add Task\n2. View List\n3. Remove Task\n4. Exit\n>> '
    choice = input(menu_list)
    return choice


def add_item():
    name = input('Enter name of task: ')
    task = input('Enter Task: ')
    due_date = input('Enter Due date: ')
    with open('To-Do.txt', 'a+') as write:
        write.seek(0)
        data = write.read()
        if len(data) > 0:
            write.write('\n')

        write.write(name + ':' + task + ':' + due_date)


def populate_todo_list():
    to_do_list.clear()
    with open('To-Do.txt', 'r') as reader:
        reader.seek(0)
        for line in reader.readlines():
            lists = line.split(':')
            to_do_list.append(lists)


def view_details():
    populate_todo_list()
    if len(to_do_list) == 0:
        print('You have no to do tasks yet.')
    else:
        print('\nTo Do List')
        for i in range(0, len(to_do_list)):
            print(to_do_list[i][0] + ': ' + to_do_list[i][1] + ' on ' + to_do_list[i][2], end='')
        print()  # This line is only intended for formatting output


def remove_item():
    populate_todo_list()
    if len(to_do_list) == 0:
        print('You have no to tasks to begin with.')
    else:
        index = -1
        item = input('Enter name of task to remove: ').lower()
        for i in range(0, len(to_do_list)):
            if to_do_list[i][0].lower() == item:
                index = i
        if index == -1:
            print('Sorry, task not found.')
        else:
            with open('To-Do.txt', 'r') as read:
                rows = read.readlines()
            rows.pop(index)
            rows[-1] = rows[-1][:-1]
            with open('To-Do.txt', 'w') as write:
                write.writelines(rows)

            print('Task has been successfully removed.')


print('<-- To Do List -->')
next_choice = menu()

while next_choice != '4':

    if next_choice == '1':
        add_item()
        next_choice = menu()

    elif next_choice == '2':
        view_details()
        next_choice = menu()
    elif next_choice == '3':
        remove_item()
        next_choice = menu()
    elif next_choice == '4':
        break
    else:
        print('You have chosen the wrong input. Try Again.')
        next_choice = menu()
