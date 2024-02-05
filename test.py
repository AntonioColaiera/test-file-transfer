import os
import unittest

def create_folder(folder_name):
    # Create a folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def create_subfolders(parent_folder, year, num_subfolders):
    # Create subfolders in the parent folder
    for i in range(num_subfolders):
        subfolder_name = os.path.join(parent_folder, f'{year}_{i+1}')
        create_folder(subfolder_name)

class TestCreateFolders(unittest.TestCase):
    def test_create_folder(self):
        # Test that a folder is created
        create_folder('test_folder')
        self.assertTrue(os.path.exists('test_folder'))
        # Clean up
        os.rmdir('test_folder')

    def test_create_subfolders(self):
        # Test that the correct number of subfolders are created
        create_subfolders('test_folder', 2023, 5)
        self.assertEqual(len(os.listdir('test_folder')), 5)
        # Clean up
        for subfolder in os.listdir('test_folder'):
            os.rmdir(os.path.join('test_folder', subfolder))
        os.rmdir('test_folder')

# Run the tests
if __name__ == '__main__':
    unittest.main()
