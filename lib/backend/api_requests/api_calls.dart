import 'dart:convert';
import 'package:flutter/foundation.dart';

import '/flutter_flow/flutter_flow_util.dart';
import 'api_manager.dart';

export 'api_manager.dart' show ApiCallResponse;

const _kPrivateApiFunctionName = 'ffPrivateApiCall';

class AddProductCall {
  static Future<ApiCallResponse> call({
    String? productName = '',
    int? stock,
    double? price,
    String? barcode = '',
  }) async {
    final ffApiRequestBody = '''
{
  "product_name": "$productName",
  "stock": $stock,
  "price": $price,
  "barcode": "$barcode"
}''';
    return ApiManager.instance.makeApiCall(
      callName: 'Add Product',
      apiUrl: 'https://scanit-xpy-bb31e6546436.herokuapp.com/add_product',
      callType: ApiCallType.POST,
      headers: {
        'Content-Type': 'application/json',
      },
      params: {},
      body: ffApiRequestBody,
      bodyType: BodyType.JSON,
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      isStreamingApi: false,
      alwaysAllowBody: false,
    );
  }
}

class GetInventoryCall {
  static Future<ApiCallResponse> call() async {
    return ApiManager.instance.makeApiCall(
      callName: 'Get Inventory',
      apiUrl: 'https://scanit-xpy-bb31e6546436.herokuapp.com/fetch_inventory',
      callType: ApiCallType.GET,
      headers: {
        'Content-Type': 'application/json',
      },
      params: {},
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      isStreamingApi: false,
      alwaysAllowBody: false,
    );
  }

  static List<String>? barcode(dynamic response) => (getJsonField(
        response,
        r'''$[:].barcode''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<String>(x))
          .withoutNulls
          .toList();
  static List<double>? price(dynamic response) => (getJsonField(
        response,
        r'''$[:].price''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<double>(x))
          .withoutNulls
          .toList();
  static List<int>? productID(dynamic response) => (getJsonField(
        response,
        r'''$[:].product_id''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<int>(x))
          .withoutNulls
          .toList();
  static List<String>? productName(dynamic response) => (getJsonField(
        response,
        r'''$[:].product_name''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<String>(x))
          .withoutNulls
          .toList();
  static List<int>? stock(dynamic response) => (getJsonField(
        response,
        r'''$[:].stock''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<int>(x))
          .withoutNulls
          .toList();
}

class NotifyLowStockCall {
  static Future<ApiCallResponse> call() async {
    return ApiManager.instance.makeApiCall(
      callName: 'Notify Low Stock',
      apiUrl: 'https://scanit-xpy-bb31e6546436.herokuapp.com/notify_low_stock',
      callType: ApiCallType.GET,
      headers: {
        'Content-Type': 'application/json',
      },
      params: {},
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      isStreamingApi: false,
      alwaysAllowBody: false,
    );
  }

  static List<String>? nameLowStock(dynamic response) => (getJsonField(
        response,
        r'''$.low_stock_items[:].product_name''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<String>(x))
          .withoutNulls
          .toList();
  static List<int>? stockLowStock(dynamic response) => (getJsonField(
        response,
        r'''$.low_stock_items[:].stock''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<int>(x))
          .withoutNulls
          .toList();
}

class CashlessTransactionCall {
  static Future<ApiCallResponse> call({
    List<String>? barcodeList,
    List<int>? quantityList,
    String? paymentMethod = 'qrph',
    String? cashReceived = 'done',
  }) async {
    final barcode = _serializeList(barcodeList);
    final quantity = _serializeList(quantityList);

    final ffApiRequestBody = '''
{
  "barcodes": $barcode,
  "quantities": $quantity,
  "payment_method": "$paymentMethod",
  "cash_received": "$cashReceived"
}''';
    return ApiManager.instance.makeApiCall(
      callName: 'Cashless Transaction',
      apiUrl:
          'https://scanit-xpy-bb31e6546436.herokuapp.com/handle_transaction',
      callType: ApiCallType.POST,
      headers: {
        'Content-Type': 'application/json',
      },
      params: {},
      body: ffApiRequestBody,
      bodyType: BodyType.JSON,
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      isStreamingApi: false,
      alwaysAllowBody: false,
    );
  }

  static String? message(dynamic response) => castToType<String>(getJsonField(
        response,
        r'''$.message''',
      ));
  static String? qrlink(dynamic response) => castToType<String>(getJsonField(
        response,
        r'''$.qr_code_url''',
      ));
}

class TotalSalesCall {
  static Future<ApiCallResponse> call() async {
    return ApiManager.instance.makeApiCall(
      callName: 'Total Sales',
      apiUrl: 'https://scanit-xpy-bb31e6546436.herokuapp.com/total_sales',
      callType: ApiCallType.GET,
      headers: {
        'Content-Type': 'application/json',
      },
      params: {},
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      isStreamingApi: false,
      alwaysAllowBody: false,
    );
  }

  static double? totalSales(dynamic response) =>
      castToType<double>(getJsonField(
        response,
        r'''$''',
      ));
}

class TransactionsByDateCall {
  static Future<ApiCallResponse> call({
    String? date = '',
  }) async {
    return ApiManager.instance.makeApiCall(
      callName: 'Transactions By Date',
      apiUrl:
          'https://scanit-xpy-bb31e6546436.herokuapp.com/transactions_by_date?date=$date',
      callType: ApiCallType.GET,
      headers: {},
      params: {},
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      isStreamingApi: false,
      alwaysAllowBody: false,
    );
  }

  static List<String>? productName(dynamic response) => (getJsonField(
        response,
        r'''$[:].items''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<String>(x))
          .withoutNulls
          .toList();
  static List<String>? paymentMethod(dynamic response) => (getJsonField(
        response,
        r'''$[:].payment_method''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<String>(x))
          .withoutNulls
          .toList();
  static List<double>? totalTransactionAmount(dynamic response) =>
      (getJsonField(
        response,
        r'''$[:].total_amount''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<double>(x))
          .withoutNulls
          .toList();
  static List<String>? dateTime(dynamic response) => (getJsonField(
        response,
        r'''$[:].transaction_date''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<String>(x))
          .withoutNulls
          .toList();
  static List<String>? transactionID(dynamic response) => (getJsonField(
        response,
        r'''$[:].transaction_id''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<String>(x))
          .withoutNulls
          .toList();
}

class MostSoldProductsCall {
  static Future<ApiCallResponse> call() async {
    return ApiManager.instance.makeApiCall(
      callName: 'Most Sold Products',
      apiUrl:
          'https://scanit-xpy-bb31e6546436.herokuapp.com/most_sold_products',
      callType: ApiCallType.GET,
      headers: {
        'Content-Type': 'application/json',
      },
      params: {},
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      isStreamingApi: false,
      alwaysAllowBody: false,
    );
  }

  static List<String>? barcode(dynamic response) => (getJsonField(
        response,
        r'''$[:].barcode''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<String>(x))
          .withoutNulls
          .toList();
  static List<String>? productName(dynamic response) => (getJsonField(
        response,
        r'''$[:].product_name''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<String>(x))
          .withoutNulls
          .toList();
  static List<int>? amountSold(dynamic response) => (getJsonField(
        response,
        r'''$[:].quantity_sold''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<int>(x))
          .withoutNulls
          .toList();
}

class SalesByDateCall {
  static Future<ApiCallResponse> call() async {
    return ApiManager.instance.makeApiCall(
      callName: 'Sales By Date',
      apiUrl: 'https://scanit-xpy-bb31e6546436.herokuapp.com/sales_by_date',
      callType: ApiCallType.GET,
      headers: {
        'Content-Type': 'application/json',
      },
      params: {},
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      isStreamingApi: false,
      alwaysAllowBody: false,
    );
  }

  static List<String>? date(dynamic response) => (getJsonField(
        response,
        r'''$[:].date''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<String>(x))
          .withoutNulls
          .toList();
  static List<double>? salesPrice(dynamic response) => (getJsonField(
        response,
        r'''$[:].total_sales''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<double>(x))
          .withoutNulls
          .toList();
}

class UpdateStockCall {
  static Future<ApiCallResponse> call({
    String? barcode = '',
    int? stock,
  }) async {
    final ffApiRequestBody = '''
{
  "barcode": "${escapeStringForJson(barcode)}",
  "new_stock": $stock
}''';
    return ApiManager.instance.makeApiCall(
      callName: 'Update Stock',
      apiUrl: 'https://scanit-xpy-bb31e6546436.herokuapp.com/update_stock',
      callType: ApiCallType.POST,
      headers: {},
      params: {},
      body: ffApiRequestBody,
      bodyType: BodyType.JSON,
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      isStreamingApi: false,
      alwaysAllowBody: false,
    );
  }

  static String? response(dynamic response) => castToType<String>(getJsonField(
        response,
        r'''$.message''',
      ));
}

class AverageTransactionValueCall {
  static Future<ApiCallResponse> call() async {
    return ApiManager.instance.makeApiCall(
      callName: 'Average Transaction Value',
      apiUrl:
          'https://scanit-xpy-bb31e6546436.herokuapp.com/average_transaction_value',
      callType: ApiCallType.GET,
      headers: {
        'Content-Type': 'application/json',
      },
      params: {},
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      isStreamingApi: false,
      alwaysAllowBody: false,
    );
  }

  static double? aveTransactionValue(dynamic response) =>
      castToType<double>(getJsonField(
        response,
        r'''$''',
      ));
}

class CashTransactionOneCall {
  static Future<ApiCallResponse> call({
    List<String>? barcodeList,
    List<int>? quantityList,
    String? paymentMethod = 'cash',
    double? cashReceived,
  }) async {
    final barcode = _serializeList(barcodeList);
    final quantity = _serializeList(quantityList);

    final ffApiRequestBody = '''
{
  "barcodes": $barcode,
  "quantities": $quantity,
  "payment_method": "${escapeStringForJson(paymentMethod)}",
  "cash_received": $cashReceived
}''';
    return ApiManager.instance.makeApiCall(
      callName: 'Cash Transaction One',
      apiUrl:
          'https://scanit-xpy-bb31e6546436.herokuapp.com/handle_transaction',
      callType: ApiCallType.POST,
      headers: {},
      params: {},
      body: ffApiRequestBody,
      bodyType: BodyType.JSON,
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      isStreamingApi: false,
      alwaysAllowBody: false,
    );
  }

  static double? change(dynamic response) => castToType<double>(getJsonField(
        response,
        r'''$.change''',
      ));
  static String? message(dynamic response) => castToType<String>(getJsonField(
        response,
        r'''$.message''',
      ));
  static String? paymentMethod(dynamic response) =>
      castToType<String>(getJsonField(
        response,
        r'''$.payment_method''',
      ));
  static double? totalAmount(dynamic response) =>
      castToType<double>(getJsonField(
        response,
        r'''$.total_amount''',
      ));
}

class GetNamesFromBarcodeCall {
  static Future<ApiCallResponse> call({
    List<String>? barcodeList,
  }) async {
    final barcode = _serializeList(barcodeList);

    final ffApiRequestBody = '''
{
  "barcodes": $barcode
}''';
    return ApiManager.instance.makeApiCall(
      callName: 'Get Names from Barcode',
      apiUrl: 'https://scanit-xpy-bb31e6546436.herokuapp.com/get_product_names',
      callType: ApiCallType.POST,
      headers: {},
      params: {},
      body: ffApiRequestBody,
      bodyType: BodyType.JSON,
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      isStreamingApi: false,
      alwaysAllowBody: false,
    );
  }

  static List<String>? productNames(dynamic response) => (getJsonField(
        response,
        r'''$''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<String>(x))
          .withoutNulls
          .toList();
}

class GetPriceFromBarcodeCall {
  static Future<ApiCallResponse> call({
    List<String>? barcodeList,
  }) async {
    final barcode = _serializeList(barcodeList);

    final ffApiRequestBody = '''
{
  "barcodes": $barcode
}''';
    return ApiManager.instance.makeApiCall(
      callName: 'Get Price from Barcode',
      apiUrl: 'https://scanit-xpy-bb31e6546436.herokuapp.com/get_prices',
      callType: ApiCallType.POST,
      headers: {},
      params: {},
      body: ffApiRequestBody,
      bodyType: BodyType.JSON,
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      isStreamingApi: false,
      alwaysAllowBody: false,
    );
  }

  static List<String>? barcode(dynamic response) => (getJsonField(
        response,
        r'''$[:].barcode''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<String>(x))
          .withoutNulls
          .toList();
  static List<double>? respectivePrices(dynamic response) => (getJsonField(
        response,
        r'''$[:].price''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<double>(x))
          .withoutNulls
          .toList();
}

class CalculateTotalCall {
  static Future<ApiCallResponse> call({
    List<String>? barcodesList,
    List<int>? quantitiesList,
  }) async {
    final barcodes = _serializeList(barcodesList);
    final quantities = _serializeList(quantitiesList);

    final ffApiRequestBody = '''
{
  "barcodes": $barcodes,
  "quantities": $quantities
}''';
    return ApiManager.instance.makeApiCall(
      callName: 'Calculate Total',
      apiUrl: 'https://scanit-xpy-bb31e6546436.herokuapp.com/calculate_total',
      callType: ApiCallType.POST,
      headers: {},
      params: {},
      body: ffApiRequestBody,
      bodyType: BodyType.JSON,
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      isStreamingApi: false,
      alwaysAllowBody: false,
    );
  }

  static double? totalAmount(dynamic response) =>
      castToType<double>(getJsonField(
        response,
        r'''$.total_amount''',
      ));
}

class ApiPagingParams {
  int nextPageNumber = 0;
  int numItems = 0;
  dynamic lastResponse;

  ApiPagingParams({
    required this.nextPageNumber,
    required this.numItems,
    required this.lastResponse,
  });

  @override
  String toString() =>
      'PagingParams(nextPageNumber: $nextPageNumber, numItems: $numItems, lastResponse: $lastResponse,)';
}

String _toEncodable(dynamic item) {
  return item;
}

String _serializeList(List? list) {
  list ??= <String>[];
  try {
    return json.encode(list, toEncodable: _toEncodable);
  } catch (_) {
    if (kDebugMode) {
      print("List serialization failed. Returning empty list.");
    }
    return '[]';
  }
}

String _serializeJson(dynamic jsonVar, [bool isList = false]) {
  jsonVar ??= (isList ? [] : {});
  try {
    return json.encode(jsonVar, toEncodable: _toEncodable);
  } catch (_) {
    if (kDebugMode) {
      print("Json serialization failed. Returning empty json.");
    }
    return isList ? '[]' : '{}';
  }
}

String? escapeStringForJson(String? input) {
  if (input == null) {
    return null;
  }
  return input
      .replaceAll('\\', '\\\\')
      .replaceAll('"', '\\"')
      .replaceAll('\n', '\\n')
      .replaceAll('\t', '\\t');
}
