// ignore_for_file: unnecessary_getters_setters

import '/backend/schema/util/schema_util.dart';

import 'index.dart';
import '/flutter_flow/flutter_flow_util.dart';

class HeheStruct extends BaseStruct {
  HeheStruct({
    String? hehe,
  }) : _hehe = hehe;

  // "hehe" field.
  String? _hehe;
  String get hehe => _hehe ?? '';
  set hehe(String? val) => _hehe = val;

  bool hasHehe() => _hehe != null;

  static HeheStruct fromMap(Map<String, dynamic> data) => HeheStruct(
        hehe: data['hehe'] as String?,
      );

  static HeheStruct? maybeFromMap(dynamic data) =>
      data is Map ? HeheStruct.fromMap(data.cast<String, dynamic>()) : null;

  Map<String, dynamic> toMap() => {
        'hehe': _hehe,
      }.withoutNulls;

  @override
  Map<String, dynamic> toSerializableMap() => {
        'hehe': serializeParam(
          _hehe,
          ParamType.String,
        ),
      }.withoutNulls;

  static HeheStruct fromSerializableMap(Map<String, dynamic> data) =>
      HeheStruct(
        hehe: deserializeParam(
          data['hehe'],
          ParamType.String,
          false,
        ),
      );

  @override
  String toString() => 'HeheStruct(${toMap()})';

  @override
  bool operator ==(Object other) {
    return other is HeheStruct && hehe == other.hehe;
  }

  @override
  int get hashCode => const ListEquality().hash([hehe]);
}

HeheStruct createHeheStruct({
  String? hehe,
}) =>
    HeheStruct(
      hehe: hehe,
    );
