import 'package:sqflite/sqflite.dart';

/// BEGIN ADD ITEM
Future performAddItem(
  Database database, {
  String? code,
  String? productName,
  int? retailPrice,
  int? storePrice,
  int? ilan,
}) {
  final query = '''
INSERT INTO inventory ("ProductBC", "ProductN", "ProductSRP", "ProductSP", "ProductQ") 
VALUES ('$code', '$productName', $retailPrice, $storePrice, $ilan);
''';
  return database.rawQuery(query);
}

/// END ADD ITEM
