import '/backend/api_requests/api_calls.dart';
import '/flutter_flow/flutter_flow_util.dart';
import 'cash_scan_page_amount_widget.dart' show CashScanPageAmountWidget;
import 'package:flutter/material.dart';

class CashScanPageAmountModel
    extends FlutterFlowModel<CashScanPageAmountWidget> {
  ///  State fields for stateful widgets in this page.

  // State field(s) for TextField widget.
  FocusNode? textFieldFocusNode;
  TextEditingController? textController;
  String? Function(BuildContext, String?)? textControllerValidator;
  // Stores action output result for [Backend Call - API (Cash Transaction One)] action in Container widget.
  ApiCallResponse? apiResult5xr;

  @override
  void initState(BuildContext context) {}

  @override
  void dispose() {
    textFieldFocusNode?.dispose();
    textController?.dispose();
  }
}
