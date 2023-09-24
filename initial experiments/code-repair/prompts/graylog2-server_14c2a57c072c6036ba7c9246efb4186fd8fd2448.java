/*
 * Copyright 2013 TORCH UG
 *
 * This file is part of Graylog2.
 *
 * Graylog2 is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * Graylog2 is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with Graylog2.  If not, see <http://www.gnu.org/licenses/>.
 */
package controllers;

import com.google.gson.annotations.SerializedName;
import com.google.inject.Inject;
import lib.APIException;
import lib.ServerNodes;
import lib.Graylog2ServerUnavailableException;
import lib.security.RedirectAuthenticator;
import models.LoginRequest;
import models.UserService;
import models.api.requests.ApiRequest;
import org.apache.shiro.SecurityUtils;
import org.apache.shiro.authc.AuthenticationException;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import play.data.Form;
import play.libs.Crypto;
import play.mvc.Http;
import play.mvc.Result;
import play.mvc.Security;

import java.io.IOException;
import java.util.Date;

import static play.data.Form.form;

public class SessionsController extends BaseController {
	private static final Logger log = LoggerFactory.getLogger(SessionsController.class);

	final static Form<LoginRequest> userForm = form(LoginRequest.class);

    @Inject
    ServerNodes serverNodes;
	@Inject
    RedirectAuthenticator authenticator;

	public Result index(String destination) {
        // Redirect if already logged in.
        String loggedInUserName = authenticator.getUsername(ctx());
        if (loggedInUserName != null) {
            log.debug("User {} already authenticated, redirecting to /", loggedInUserName);
            if (destination != null && !destination.isEmpty()) {
                return redirect(destination);
            } else {
                return redirect("/");
            }
        }
        if (session("username") != null && !session("username").isEmpty()) {
            if (destination != null && !destination.isEmpty()) {
                return redirect(destination);
            } else {
                return redirect("/");
            }
        }
        checkServerConnections();
        return ok(views.html.sessions.login.render(userForm, !serverNodes.isConnected(), destination));
    }

    private void checkServerConnections() {
        if (!serverNodes.isConnected()) {
            flash("error", "No Graylog2 servers available. Cannot log in.");
        }
    }

    public Result create() {
		Form<LoginRequest> loginRequest = userForm.bindFromRequest();

		if (loginRequest.hasErrors()) {
			flash("error", "Please fill out all fields.");
            return badRequest(views.html.sessions.login.render(loginRequest, !serverNodes.isConnected(), loginRequest.field("destination").value()));
		}
		
		LoginRequest r = loginRequest.get();

        try {
            final SessionResponse sessionResponse = api().post(SessionResponse.class)
                    .path("/system/sessions")
                    .unauthenticated()
                    .body(new SessionCreateRequest(r.username, r.password, request().remoteAddress()))
                    .execute();
            // if we have successfully created a session, we can save that id for the next request
            final String cookieContent = Crypto.encryptAES(r.username + "\t" + sessionResponse.sessionId);
            Http.Context.current().session().put("sessionid", cookieContent);

            // if we were redirected from somewhere else because the session had expired, redirect back to that page
            // otherwise use the configured startpage (or skip it if that was requested)
            if (r.destination != null