#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for data in dir(hidden_4):
        if data[0] != '_' and data[1] != '_':
            print(data)