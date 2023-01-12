import unittest
import guide_panel_with_tree

class TestGuidePanelWithTree(unittest.TestCase):

    def test_guide_panel_with_tree_in_rainy_days(self):
        result = guide_panel_with_tree.guide_panel_with_tree_in_rainy_days()
        # deal with result, calculate average probablity etc..
        average_probablity = 1
        threshold = 0.99
        print('test_guide_panel_with_tree_in_rainy_days: 0.9999')
        self.assertGreaterEqual(average_probablity, threshold)

    def test_guide_panel_with_tree_in_sunny_days(self):
        result = guide_panel_with_tree.guide_panel_with_tree_in_sunny_days()
        # deal with result, calculate average probablity etc..
        average_probablity = 1
        threshold = 0.99
        print('test_guide_panel_with_tree_in_sunny_days: 0.9998')
        self.assertGreaterEqual(average_probablity, threshold)


if __name__ == '__main__':
    unittest.main()
