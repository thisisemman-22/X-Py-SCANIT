import 'package:rxdart/rxdart.dart';

import 'custom_auth_manager.dart';

class ApiVersionAuthUser {
  ApiVersionAuthUser({required this.loggedIn, this.uid});

  bool loggedIn;
  String? uid;
}

/// Generates a stream of the authenticated user.
BehaviorSubject<ApiVersionAuthUser> apiVersionAuthUserSubject =
    BehaviorSubject.seeded(ApiVersionAuthUser(loggedIn: false));
Stream<ApiVersionAuthUser> apiVersionAuthUserStream() =>
    apiVersionAuthUserSubject
        .asBroadcastStream()
        .map((user) => currentUser = user);
