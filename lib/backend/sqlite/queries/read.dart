import '/backend/sqlite/queries/sqlite_row.dart';
import 'package:sqflite/sqflite.dart';

Future<List<T>> _readQuery<T>(
  Database database,
  String query,
  T Function(Map<String, dynamic>) create,
) =>
    database.rawQuery(query).then((r) => r.map((e) => create(e)).toList());

/// BEGIN GET INVENTORY DATA
Future<List<GetInventoryDataRow>> performGetInventoryData(
  Database database,
) {
  const query = '''
SELECT * FROM inventory order by product_dn
''';
  return _readQuery(database, query, (d) => GetInventoryDataRow(d));
}

class GetInventoryDataRow extends SqliteRow {
  GetInventoryDataRow(super.data);

  int? get productDn => data['product_dn'] as int?;
  String get productBc => data['product_bc'] as String;
  String get productN => data['product_n'] as String;
  int get productSrp => data['product_srp'] as int;
  int get productSp => data['product_sp'] as int;
  String get productQ => data['product_q'] as String;
}

/// END GET INVENTORY DATA
