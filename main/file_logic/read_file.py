def read_file(file_name):
    """Reads the data in a text file

        Parameters
        ----------
        file_name : str
            The name and path of the file to be read

        Returns
        ------
            list: A list with each item being a line from the file
        """
    with open(file_name) as f:
        return f.readlines()
