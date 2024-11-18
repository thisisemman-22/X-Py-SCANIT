import 'package:flutter/material.dart';

class FFAppState extends ChangeNotifier {
  static FFAppState _instance = FFAppState._internal();

  factory FFAppState() {
    return _instance;
  }

  FFAppState._internal();

  static void reset() {
    _instance = FFAppState._internal();
  }

  Future initializePersistedState() async {}

  void update(VoidCallback callback) {
    callback();
    notifyListeners();
  }

  List<String> _scannedItemsList = [];
  List<String> get scannedItemsList => _scannedItemsList;
  set scannedItemsList(List<String> value) {
    _scannedItemsList = value;
  }

  void addToScannedItemsList(String value) {
    scannedItemsList.add(value);
  }

  void removeFromScannedItemsList(String value) {
    scannedItemsList.remove(value);
  }

  void removeAtIndexFromScannedItemsList(int index) {
    scannedItemsList.removeAt(index);
  }

  void updateScannedItemsListAtIndex(
    int index,
    String Function(String) updateFn,
  ) {
    scannedItemsList[index] = updateFn(_scannedItemsList[index]);
  }

  void insertAtIndexInScannedItemsList(int index, String value) {
    scannedItemsList.insert(index, value);
  }

  List<String> _inventoryList = [];
  List<String> get inventoryList => _inventoryList;
  set inventoryList(List<String> value) {
    _inventoryList = value;
  }

  void addToInventoryList(String value) {
    inventoryList.add(value);
  }

  void removeFromInventoryList(String value) {
    inventoryList.remove(value);
  }

  void removeAtIndexFromInventoryList(int index) {
    inventoryList.removeAt(index);
  }

  void updateInventoryListAtIndex(
    int index,
    String Function(String) updateFn,
  ) {
    inventoryList[index] = updateFn(_inventoryList[index]);
  }

  void insertAtIndexInInventoryList(int index, String value) {
    inventoryList.insert(index, value);
  }

  String _qrCodeURL = '';
  String get qrCodeURL => _qrCodeURL;
  set qrCodeURL(String value) {
    _qrCodeURL = value;
  }

  List<int> _scannedItemsQuantity = [];
  List<int> get scannedItemsQuantity => _scannedItemsQuantity;
  set scannedItemsQuantity(List<int> value) {
    _scannedItemsQuantity = value;
  }

  void addToScannedItemsQuantity(int value) {
    scannedItemsQuantity.add(value);
  }

  void removeFromScannedItemsQuantity(int value) {
    scannedItemsQuantity.remove(value);
  }

  void removeAtIndexFromScannedItemsQuantity(int index) {
    scannedItemsQuantity.removeAt(index);
  }

  void updateScannedItemsQuantityAtIndex(
    int index,
    int Function(int) updateFn,
  ) {
    scannedItemsQuantity[index] = updateFn(_scannedItemsQuantity[index]);
  }

  void insertAtIndexInScannedItemsQuantity(int index, int value) {
    scannedItemsQuantity.insert(index, value);
  }

  List<String> _listOfJSON = [];
  List<String> get listOfJSON => _listOfJSON;
  set listOfJSON(List<String> value) {
    _listOfJSON = value;
  }

  void addToListOfJSON(String value) {
    listOfJSON.add(value);
  }

  void removeFromListOfJSON(String value) {
    listOfJSON.remove(value);
  }

  void removeAtIndexFromListOfJSON(int index) {
    listOfJSON.removeAt(index);
  }

  void updateListOfJSONAtIndex(
    int index,
    String Function(String) updateFn,
  ) {
    listOfJSON[index] = updateFn(_listOfJSON[index]);
  }

  void insertAtIndexInListOfJSON(int index, String value) {
    listOfJSON.insert(index, value);
  }

  String _singleItem = '';
  String get singleItem => _singleItem;
  set singleItem(String value) {
    _singleItem = value;
  }

  int _singleQuantity = 0;
  int get singleQuantity => _singleQuantity;
  set singleQuantity(int value) {
    _singleQuantity = value;
  }

  double _singleTotalAmount = 0.0;
  double get singleTotalAmount => _singleTotalAmount;
  set singleTotalAmount(double value) {
    _singleTotalAmount = value;
  }

  double _singleChange = 0.0;
  double get singleChange => _singleChange;
  set singleChange(double value) {
    _singleChange = value;
  }

  String _num1 = '';
  String get num1 => _num1;
  set num1(String value) {
    _num1 = value;
  }

  String _num2 = '';
  String get num2 => _num2;
  set num2(String value) {
    _num2 = value;
  }

  String _answer = '';
  String get answer => _answer;
  set answer(String value) {
    _answer = value;
  }
}
