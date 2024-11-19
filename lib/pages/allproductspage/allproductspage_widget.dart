import '/backend/api_requests/api_calls.dart';
import '/flutter_flow/flutter_flow_icon_button.dart';
import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';
import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'allproductspage_model.dart';
export 'allproductspage_model.dart';

class AllproductspageWidget extends StatefulWidget {
  const AllproductspageWidget({super.key});

  @override
  State<AllproductspageWidget> createState() => _AllproductspageWidgetState();
}

class _AllproductspageWidgetState extends State<AllproductspageWidget> {
  late AllproductspageModel _model;

  final scaffoldKey = GlobalKey<ScaffoldState>();

  @override
  void initState() {
    super.initState();
    _model = createModel(context, () => AllproductspageModel());
  }

  @override
  void dispose() {
    _model.dispose();

    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () => FocusScope.of(context).unfocus(),
      child: Scaffold(
        key: scaffoldKey,
        backgroundColor: const Color(0xFF28292A),
        appBar: PreferredSize(
          preferredSize: const Size.fromHeight(80.0),
          child: AppBar(
            backgroundColor: const Color(0xFF717171),
            automaticallyImplyLeading: false,
            leading: Align(
              alignment: const AlignmentDirectional(0.0, 10.0),
              child: Padding(
                padding: const EdgeInsetsDirectional.fromSTEB(40.0, 15.0, 0.0, 0.0),
                child: FlutterFlowIconButton(
                  borderColor: Colors.transparent,
                  borderRadius: 8.0,
                  buttonSize: 100.0,
                  icon: Icon(
                    Icons.person_outline_rounded,
                    color: FlutterFlowTheme.of(context).info,
                    size: 30.0,
                  ),
                  onPressed: () async {
                    context.pushNamed('profile_page');
                  },
                ),
              ),
            ),
            title: Align(
              alignment: const AlignmentDirectional(0.0, 0.0),
              child: Padding(
                padding: const EdgeInsetsDirectional.fromSTEB(20.0, 20.0, 0.0, 0.0),
                child: Text(
                  'PRODUCTS',
                  style: FlutterFlowTheme.of(context).headlineMedium.override(
                        fontFamily: 'Poppins',
                        color: const Color(0xFF02E083),
                        fontSize: 22.0,
                        letterSpacing: 0.0,
                      ),
                ),
              ),
            ),
            actions: [
              Padding(
                padding: const EdgeInsetsDirectional.fromSTEB(0.0, 20.0, 25.0, 0.0),
                child: FlutterFlowIconButton(
                  borderColor: Colors.transparent,
                  borderRadius: 8.0,
                  buttonSize: 40.0,
                  icon: Icon(
                    Icons.notifications_sharp,
                    color: FlutterFlowTheme.of(context).info,
                    size: 30.0,
                  ),
                  onPressed: () async {
                    await showDialog(
                      context: context,
                      builder: (alertDialogContext) {
                        return AlertDialog(
                          title: const Text('No New Notifications'),
                          content: const Text('You have no new notifications. '),
                          actions: [
                            TextButton(
                              onPressed: () =>
                                  Navigator.pop(alertDialogContext),
                              child: const Text('Ok'),
                            ),
                          ],
                        );
                      },
                    );
                  },
                ),
              ),
            ],
            bottom: PreferredSize(
              preferredSize: const Size.fromHeight(100.0),
              child: Container(),
            ),
            centerTitle: false,
            elevation: 2.0,
          ),
        ),
        body: SafeArea(
          top: true,
          child: Stack(
            alignment: const AlignmentDirectional(0.0, 0.0),
            children: [
              Align(
                alignment: const AlignmentDirectional(0.0, -1.0),
                child: SingleChildScrollView(
                  primary: false,
                  child: Column(
                    mainAxisSize: MainAxisSize.max,
                    mainAxisAlignment: MainAxisAlignment.start,
                    crossAxisAlignment: CrossAxisAlignment.center,
                    children: [
                      Row(
                        mainAxisSize: MainAxisSize.max,
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Align(
                            alignment: const AlignmentDirectional(0.0, 0.0),
                            child: Container(
                              width: 400.0,
                              decoration: const BoxDecoration(
                                color: Color(0xFF28292A),
                              ),
                            ),
                          ),
                        ],
                      ),
                      Align(
                        alignment: const AlignmentDirectional(0.0, 0.0),
                        child: Padding(
                          padding: const EdgeInsetsDirectional.fromSTEB(
                              0.0, 20.0, 0.0, 20.0),
                          child: Row(
                            mainAxisSize: MainAxisSize.max,
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [
                              Flexible(
                                child: Align(
                                  alignment: const AlignmentDirectional(0.0, 0.0),
                                  child: InkWell(
                                    splashColor: Colors.transparent,
                                    focusColor: Colors.transparent,
                                    hoverColor: Colors.transparent,
                                    highlightColor: Colors.transparent,
                                    onTap: () async {
                                      context.pushNamed('updateStock');
                                    },
                                    child: Container(
                                      width: 150.0,
                                      height: 40.0,
                                      decoration: BoxDecoration(
                                        color: const Color(0xFF02E083),
                                        borderRadius:
                                            BorderRadius.circular(24.0),
                                      ),
                                      child: Align(
                                        alignment:
                                            const AlignmentDirectional(0.0, 0.0),
                                        child: Text(
                                          'Update Stock',
                                          textAlign: TextAlign.center,
                                          style: FlutterFlowTheme.of(context)
                                              .bodyMedium
                                              .override(
                                                fontFamily: 'Poppins',
                                                color: const Color(0xFF28292A),
                                                fontSize: 15.0,
                                                letterSpacing: 0.0,
                                                fontWeight: FontWeight.w600,
                                              ),
                                        ),
                                      ),
                                    ),
                                  ),
                                ),
                              ),
                              Flexible(
                                child: Align(
                                  alignment: const AlignmentDirectional(0.0, 0.0),
                                  child: InkWell(
                                    splashColor: Colors.transparent,
                                    focusColor: Colors.transparent,
                                    hoverColor: Colors.transparent,
                                    highlightColor: Colors.transparent,
                                    onTap: () async {
                                      context.pushNamed(
                                          'inventory_view_all_add_item_page');
                                    },
                                    child: Container(
                                      width: 150.0,
                                      height: 40.0,
                                      decoration: BoxDecoration(
                                        color: const Color(0xFF02E083),
                                        borderRadius:
                                            BorderRadius.circular(24.0),
                                      ),
                                      child: Align(
                                        alignment:
                                            const AlignmentDirectional(0.0, 0.0),
                                        child: Padding(
                                          padding:
                                              const EdgeInsetsDirectional.fromSTEB(
                                                  0.0, 10.0, 0.0, 10.0),
                                          child: Text(
                                            'Add Item',
                                            style: FlutterFlowTheme.of(context)
                                                .bodyMedium
                                                .override(
                                                  fontFamily: 'Poppins',
                                                  color: const Color(0xFF28292A),
                                                  fontSize: 15.0,
                                                  letterSpacing: 0.0,
                                                  fontWeight: FontWeight.w600,
                                                ),
                                          ),
                                        ),
                                      ),
                                    ),
                                  ),
                                ),
                              ),
                            ]
                                .divide(const SizedBox(width: 0.0))
                                .addToEnd(const SizedBox(width: 0.0)),
                          ),
                        ),
                      ),
                      Expanded(
                        child: Align(
                          alignment: const AlignmentDirectional(0.0, -1.0),
                          child: FutureBuilder<ApiCallResponse>(
                            future: GetInventoryCall.call(),
                            builder: (context, snapshot) {
                              // Customize what your widget looks like when it's loading.
                              if (!snapshot.hasData) {
                                return Center(
                                  child: SizedBox(
                                    width: 50.0,
                                    height: 50.0,
                                    child: CircularProgressIndicator(
                                      valueColor: AlwaysStoppedAnimation<Color>(
                                        FlutterFlowTheme.of(context).primary,
                                      ),
                                    ),
                                  ),
                                );
                              }
                              final listViewGetInventoryResponse =
                                  snapshot.data!;

                              return Builder(
                                builder: (context) {
                                  final productName =
                                      GetInventoryCall.productName(
                                            listViewGetInventoryResponse
                                                .jsonBody,
                                          )?.toList() ??
                                          [];

                                  return RefreshIndicator(
                                    color: FlutterFlowTheme.of(context).primary,
                                    onRefresh: () async {},
                                    child: ListView.builder(
                                      padding: EdgeInsets.zero,
                                      primary: false,
                                      shrinkWrap: true,
                                      scrollDirection: Axis.vertical,
                                      itemCount: productName.length,
                                      itemBuilder: (context, productNameIndex) {
                                        final productNameItem =
                                            productName[productNameIndex];
                                        return Align(
                                          alignment:
                                              const AlignmentDirectional(0.0, 0.2),
                                          child: Material(
                                            color: Colors.transparent,
                                            child: ListTile(
                                              title: Text(
                                                productNameItem,
                                                style:
                                                    FlutterFlowTheme.of(context)
                                                        .titleLarge
                                                        .override(
                                                          fontFamily: 'Poppins',
                                                          color: FlutterFlowTheme
                                                                  .of(context)
                                                              .primaryBackground,
                                                          letterSpacing: 0.0,
                                                        ),
                                              ),
                                              subtitle: Text(
                                                (GetInventoryCall.stock(
                                                  listViewGetInventoryResponse
                                                      .jsonBody,
                                                )![productNameIndex])
                                                    .toString(),
                                                style:
                                                    FlutterFlowTheme.of(context)
                                                        .labelSmall
                                                        .override(
                                                          fontFamily: 'Poppins',
                                                          color: FlutterFlowTheme
                                                                  .of(context)
                                                              .alternate,
                                                          letterSpacing: 0.0,
                                                        ),
                                              ),
                                              tileColor: const Color(0xFF28292A),
                                              dense: false,
                                            ),
                                          ),
                                        );
                                      },
                                    ),
                                  );
                                },
                              );
                            },
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
              Align(
                alignment: const AlignmentDirectional(0.0, 1.12),
                child: SafeArea(
                  child: Container(
                    height: 125.0,
                    decoration: const BoxDecoration(
                      color: Color(0xFF717171),
                      boxShadow: [
                        BoxShadow(
                          blurRadius: 20.0,
                          color: Color(0x33000000),
                          offset: Offset(
                            0.0,
                            2.0,
                          ),
                          spreadRadius: 5.0,
                        )
                      ],
                    ),
                    child: Row(
                      mainAxisSize: MainAxisSize.max,
                      mainAxisAlignment: MainAxisAlignment.center,
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Expanded(
                          child: Align(
                            alignment: const AlignmentDirectional(0.0, 0.0),
                            child: Padding(
                              padding: const EdgeInsetsDirectional.fromSTEB(
                                  60.0, 0.0, 0.0, 43.0),
                              child: FlutterFlowIconButton(
                                borderColor: Colors.transparent,
                                borderRadius: 8.0,
                                buttonSize: 40.0,
                                fillColor: const Color(0xFF717171),
                                icon: const Icon(
                                  Icons.folder,
                                  color: Colors.white,
                                  size: 30.0,
                                ),
                                onPressed: () async {
                                  context
                                      .pushNamed('transaction_overview_page');
                                },
                              ),
                            ),
                          ),
                        ),
                        Expanded(
                          child: Align(
                            alignment: const AlignmentDirectional(0.0, 0.0),
                            child: Padding(
                              padding: const EdgeInsetsDirectional.fromSTEB(
                                  30.0, 0.0, 30.0, 40.0),
                              child: FlutterFlowIconButton(
                                borderColor: Colors.transparent,
                                borderRadius: 8.0,
                                buttonSize: 66.0,
                                fillColor: const Color(0xFF717171),
                                icon: const Icon(
                                  Icons.qr_code_scanner_outlined,
                                  color: Colors.white,
                                  size: 50.0,
                                ),
                                onPressed: () async {
                                  context.pushNamed('scan_page');
                                },
                              ),
                            ),
                          ),
                        ),
                        Expanded(
                          child: Align(
                            alignment: const AlignmentDirectional(1.0, 0.0),
                            child: Padding(
                              padding: const EdgeInsetsDirectional.fromSTEB(
                                  0.0, 0.0, 80.0, 43.0),
                              child: FlutterFlowIconButton(
                                borderColor: Colors.transparent,
                                borderRadius: 8.0,
                                buttonSize: 40.0,
                                fillColor: const Color(0xFF717171),
                                icon: const FaIcon(
                                  FontAwesomeIcons.boxOpen,
                                  color: Color(0xFF02E083),
                                  size: 30.0,
                                ),
                                onPressed: () async {
                                  context.pushNamed('allproductspage');
                                },
                              ),
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
