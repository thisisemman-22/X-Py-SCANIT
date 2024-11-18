import 'dart:convert';
import 'dart:math' as math;

import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:intl/intl.dart';
import 'package:timeago/timeago.dart' as timeago;
import 'lat_lng.dart';
import 'place.dart';
import 'uploaded_file.dart';
import '/backend/sqlite/sqlite_manager.dart';
import '/auth/custom_auth/auth_util.dart';

int? getTotalStockValue() {
  int calculateTotalStockValue(List<dynamic> inventoryData) {
    int totalValue = 0;
    for (var item in inventoryData) {
      int stock =
          item['stock']?.toDouble() ?? 0; // Handle potential null values
      int price =
          item['price']?.toDouble() ?? 0; // Handle potential null values
      totalValue += stock * price;
    }
    return totalValue;
  }
}

String? getProductNameByBarcode() {
  String getProductNameByBarcode(
      List<Map<String, dynamic>> scannedItemList, String barcode) {
    // Find the item in the scannedItemList where the barcode matches
    final item = scannedItemList.firstWhere(
      (item) => item['barcode'] == barcode,
      orElse: () => <String, dynamic>{},
    );

    // Return the product name if found, otherwise return 'Not found'
    return item.isNotEmpty ? item['product_name'] ?? 'Not found' : 'Not found';
  }
}
