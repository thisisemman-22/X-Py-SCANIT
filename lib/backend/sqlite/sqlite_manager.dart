import 'package:flutter/foundation.dart';

import '/backend/sqlite/init.dart';
import 'queries/read.dart';
import 'queries/update.dart';

import 'package:sqflite/sqflite.dart';
export 'queries/read.dart';
export 'queries/update.dart';

class SQLiteManager {
  SQLiteManager._();

  static SQLiteManager? _instance;
  static SQLiteManager get instance => _instance ??= SQLiteManager._();

  static late Database _database;
  Database get database => _database;

  static Future initialize() async {
    if (kIsWeb) {
      return;
    }
    _database = await initializeDatabaseFromDbFile(
      'data',
      'hrybigdick.db',
    );
  }

  /// START READ QUERY CALLS

  Future<List<GetInventoryDataRow>> getInventoryData() =>
      performGetInventoryData(
        _database,
      );

  /// END READ QUERY CALLS

  /// START UPDATE QUERY CALLS

  Future addItem({
    String? code,
    String? productName,
    int? retailPrice,
    int? storePrice,
    int? ilan,
  }) =>
      performAddItem(
        _database,
        code: code,
        productName: productName,
        retailPrice: retailPrice,
        storePrice: storePrice,
        ilan: ilan,
      );

  /// END UPDATE QUERY CALLS
}
