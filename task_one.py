import argparse

def compare(tup):
    key, values = tup
    if "last_name" in values:
        return int(key)
    else:
        raise ValueError("Invalid input files.") 


def main(args):
    """
    Match first name and last name by id and write to output file
    """
    with open (args.input_file_one, 'r') as file_one:
        file_one_content = file_one.readlines()

    with open (args.input_file_two, 'r') as file_two:
        file_two_content = file_two.readlines()

    data = {}
    out = []
    for line in file_one_content:
        first_name, id = line.strip().split(' ')
        data[id] = { "first_name": first_name }

    for line in file_two_content:
        last_name, id = line.strip().split(' ')
        if id in data:
            data[id].update({"last_name": last_name})
        else:
            # This occurs when no first name is found for id
            raise ValueError("Invalid input files.") 

    if args.sort:
        # It's faster to sort like this than sort on insert
        out = sorted(data.items(), key=compare)
    else:
        out = data.items()

    with open (args.output_file, 'w') as file_out:
        for key, values in out:
            file_out.write(values["first_name"] + " " + values["last_name"] +  " " + key + "\n")



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Process files.")
    parser.add_argument("input_file_one", help="Input file one.")
    parser.add_argument("input_file_two", help="Input file two.")
    parser.add_argument("output_file", help="Output file.")
    parser.add_argument("--sort", action="store_true", help="Sort output by id.")
    args = parser.parse_args()
    main(args)