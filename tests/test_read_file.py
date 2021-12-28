import main.file_logic.read_file as rf;


def test_read_file():
    """Tests the read_file function

        checks to see if the read_file function opens a .txt file and returns the text as 
        a list of strings where each string contains the content of a line in the .txt document
        """
    assert rf.read_file('./tests/mock_data/textfile.txt') == ['bananas asdfa\n', 'apples 123412\n', '6 2346 gsdfg']