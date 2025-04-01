from app.io.input import input_text_from_console, read_file, read_file_pandas
from app.io.output import output_text_to_console, write_to_file

def main():

    input_text_from_console()

    read_file()

    read_file_pandas()

    output_text_to_console()

    write_to_file()

if __name__ == "__main__":
    main()