// Lust 2-26

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SalesCalculator {
    class Program {

        // List 2-25
        static void Main(string[] args) {
            var sales = new SalesCounter("sales.csv");
            var amountPerStore = sales.GetPerStoreSales();
            foreach (var obj in amountPerStore) {
                Console.WriteLine("{0} {1}", obj.Key, obj.Value);
            }
            Console.WriteLine("以上が結果です。");
            Console.ReadKey();
        }
    }
    public class Sale
    {
        // 店舗名
        public string ShopName { get; set; }

        // 商品カテゴリ
        public string ProductCategory { get; set; }

        // 売り上げ高
        public int Amount { get; set; }
    }
    public class SalesCounter
    {
        private IEnumerable<Sale> _sales;

        // コンストラクタ
        public SalesCounter(string filePath) {
            _sales = ReadSales(filePath);
        }

        // 売り上げデータを読み込み、Saleオブジェクトのリストを返す
        private static IEnumerable<Sale> ReadSales(string filePath) {
            var sales = new List<Sale>();
            var lines = File.ReadAllLines(filePath);
            foreach (var line in lines) {
                var items = line.Split(',');
                var sale = new Sale {
                    ShopName = items[0],
                    ProductCategory = items[1],
                    Amount = int.Parse(items[2])
                };
                sales.Add(sale);
            }
            return sales;
        }


        // List 2-24
        // 店舗別売り上げを求める
        public IDictionary<string, int> GetPerStoreSales() {
            var dict = new Dictionary<string, int>();
            foreach (var sale in _sales) {
                if (dict.ContainsKey(sale.ShopName))
                    dict[sale.ShopName] += sale.Amount;
                else
                    dict[sale.ShopName] = sale.Amount;
            }
            return dict;
        }
    }
}
