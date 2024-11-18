import '/backend/api_requests/api_calls.dart';
import '/flutter_flow/flutter_flow_util.dart';
import 'scan_page_transaction_widget.dart' show ScanPageTransactionWidget;
import 'package:flutter/material.dart';

class ScanPageTransactionModel
    extends FlutterFlowModel<ScanPageTransactionWidget> {
  ///  State fields for stateful widgets in this page.

  // State field(s) for TextField widget.
  FocusNode? textFieldFocusNode;
  TextEditingController? textController;
  String? Function(BuildContext, String?)? textControllerValidator;
  // State field(s) for CountController widget.
  int? countControllerValue;
  // Stores action output result for [Backend Call - API (Cashless Transaction One)] action in Text widget.
  ApiCallResponse? apiResult7d4;
  var barcoded = '';

  @override
  void initState(BuildContext context) {}

  @override
  void dispose() {
    textFieldFocusNode?.dispose();
    textController?.dispose();
  }
}
