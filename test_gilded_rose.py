# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)

    def test_quality_degrades_twice_as_fast_after_sell_date(self):
        items = [Item("Elixir of the Mongoose", 0, 10), Item("Conjured Mana Cake", 0, 6)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(8, items[0].quality)
        self.assertEqual(4, items[1].quality)  # Conjured quality degrades twice as fast

    def test_backstage_pass_should_increase_in_quality(self):
        pass_item = "Backstage passes to a TAFKAL80ETC concert"
        items = [Item(pass_item, 11, 10), Item(pass_item, 10, 10), Item(pass_item, 5, 10)]
        gr = GildedRose(items)

        gr.update_quality()

        assert items[0].sell_in == 10
        assert items[0].quality == 11

        assert items[1].sell_in == 9
        assert items[1].quality == 12

        assert items[2].sell_in == 4
        assert items[2].quality == 13

    def test_sulfuras_never_decreases_in_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(80, items[0].quality)  # Sulfuras quality never changes

if __name__ == '__main__':
    unittest.main()
