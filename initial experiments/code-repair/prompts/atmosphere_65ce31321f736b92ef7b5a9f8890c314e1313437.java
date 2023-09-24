/*
 * Copyright 2012 Jeanfrancois Arcand
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not
 * use this file except in compliance with the License. You may obtain a copy of
 * the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations under
 * the License.
 */
package org.atmosphere.cpr;

import org.atmosphere.util.FakeHttpSession;
import org.atmosphere.util.QueryStringDecoder;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import javax.servlet.AsyncContext;
import javax.servlet.DispatcherType;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.ServletInputStream;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletRequestWrapper;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import javax.servlet.http.Part;
import java.io.BufferedReader;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.StringReader;
import java.io.UnsupportedEncodingException;
import java.security.Principal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.Enumeration;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.Set;
import java.util.concurrent.atomic.AtomicBoolean;

import static org.atmosphere.cpr.HeaderConfig.X_ATMOSPHERE;

/**
 * An Atmosphere request representation. An {@link AtmosphereRequest} is a two-way communication channel between the
 * client and the server. If the {@link org.atmosphere.cpr.AtmosphereRequest#isDestroyable()} is set to false, or if its
 * associated {@link AtmosphereResource} has been suspended, this object can be re-used at any moments between requests.
 * You can use it's associated {@link AtmosphereResponse} to write bytes at any moment, making this object bi-directional.
 * <br/>
 * You can retrieve the AtmosphereResource can be retrieved as an attribute {@link FrameworkConfig#ATMOSPHERE_RESOURCE}.
 *
 * @author Jeanfrancois Arcand
 */
public class AtmosphereRequest extends HttpServletRequestWrapper {

    private Logger logger = LoggerFactory.getLogger(AtmosphereRequest.class);
    private ServletInputStream bis;
    private BufferedReader br;
    private final Builder b;
    private final AtomicBoolean destroyed = new AtomicBoolean(false);
    private boolean queryComputed = false;
    private boolean cookieComputed = false;

    private AtmosphereRequest(Builder b) {
        super(b.request == null ? new NoOpsRequest() : b.request);
        if (b.inputStream == null) {
            if (b.dataBytes != null) {
                configureStream(b.dataBytes, b.offset, b.length, b.encoding);
            } else if (b.data != null) {
                try {
                    byte[] bytes = b.data.getBytes("UTF-8");
                    bis = new ByteInputStream(bytes, 0, bytes.length);
                } catch (UnsupportedEncodingException e) {
                    logger.trace("", e);
                }
                br = new BufferedReader(new StringReader(b.data));
            }
        } else {
            bis = new IS(b.inputStream);
            br = new BufferedReader(new InputStreamReader(b.inputStream));
        }

        if (b.request == null) b.request(new NoOpsRequest());

        this.b = b;
    }

    private void configureStream(byte[] bytes, int offset, int length, String encoding) {
        bis = new ByteInputStream(bytes, offset, length);
        try {
            br = new BufferedReader(new StringReader(new String(bytes, offset, length, encoding)));
        } catch (UnsupportedEncodingException e) {
            throw new RuntimeException(e);
        }
    }

    public boolean destroyed() {
        return destroyed.get();
    }

    public AtmosphereRequest destroyable(boolean destroyable) {
        b.destroyable = destroyable;
        return this;
    }

    /**
     * {@inheritDoc}
     */
    @Override

    public String getPathInfo() {
        return b.pathInfo != "" ? b.pathInfo : isNotNoOps() ? b.request.getPathInfo() : "";
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public String getPathTranslated() {
        return b.request.getPathTranslated();
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public String getQueryString() {
        return b.queryString != "" ? b.queryString : isNotNoOps() ? b.request.getQueryString() : "";
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public String getRemoteUser() {
        return b.request.getRemoteUser();
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public String getRequestedSessionId() {
        return b.request.getRequestedSessionId();
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public String getMethod() {
        return b.methodType != null ? b.methodType : b.request.getMethod();
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public Part getPart(String name) throws IOException, ServletException {
        return b.request.getPart(name);
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public Collection<Part> getParts() throws IOException, ServletException {
        return b.request.getParts();
    }

    /**
     * {@inheritDoc}
     */

    @Override
    public String getContentType() {
        return b.contentType != null ? b.contentType : b.request.getContentType();
    }

    @Override
    public DispatcherType getDispatcherType() {
        return b.request.getDispatcherType();
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public String getServletPath() {
        return b.servletPath != "" ? b.servletPath : (isNotNoOps() ? b.request.getServletPath() : "");
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public String getRequestURI() {
        return b.requestURI != null ? b.requestURI : (isNotNoOps() ? b.request.getRequestURI() : null);
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public StringBuffer getRequestURL() {
        return b.requestURL != null ? new StringBuffer(b.requestURL) : (isNotNoOps() ? b.request.getRequestURL() : null);
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public Enumeration getHeaders(String name) {

        ArrayList list = new ArrayList<String>();
        // Never override the parent Request
        if (!name.equalsIgnoreCase("content-type")) {
            list = Collections.list(b.request.getHeaders(name));
        }

        if (name.equalsIgnoreCase("content-type")) {
            String s = getContentType();
            if (s != null) {
                list.add(s);
            }
        } else {
            if (b.headers.get(name) != null) {
                list.add(b.headers.get(name));
            }

            if (isNotNoOps()) {
                if (list.size() == 0 && name.startsWith(X_ATMOSPHERE)) {
                    if (b.request.getAttribute(name) != null) {
                        list.add(b.request.getAttribute(name));
                    }
                }
            }
        }
        return Collections.enumeration(list);
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public int getIntHeader(String name) {
        return b.request.getIntHeader(name);
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public Enumeration<String> getHeaderNames() {
        ArrayList list = Collections.list(b.request.getHeaderNames());
        if (b.contentType != null) {
            list.add("Content-Type");
        }

        if (b.request != null) {
            Enumeration e = b.request.getAttributeNames();
            while (e.hasMoreElements()) {
                String name = e.nextElement().toString();
                if (name.startsWith(X_ATMOSPHERE)) {
                    list.add(name);
                }
            }
        }

        list.addAll(b.headers.keySet());

        return Collections.enumeration(list);
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public boolean authenticate(HttpServletResponse response) throws IOException, ServletException {
        return b.request.authenticate(response);
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public String getAuthType() {
        return b.request.getAuthType();
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public String getContextPath() {
        return isNotNoOps() && b.request.getContextPath() != null ? b.request.getContextPath() : b.contextPath != null ? b.contextPath : "";
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public Cookie[] getCookies() {
        if (!cookieComputed) {
            cookieComputed = true;
            Cookie[] c = b.request.getCookies();
            if (c != null && c.length > 0) {
                b.cookies.addAll(Arrays.asList(c));
            }
        }
        return b.cookies.toArray(new Cookie[]{});
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public long getDateHeader(String name) {
        return b.request.getDateHeader(name);
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public String getHeader(String s) {
        return getHeader(s, true);
    }

    public HttpServletRequest wrappedRequest() {
        return b.request;
    }

    public String getHeader(String s, boolean checkCase) {

        if ("content-type".equalsIgnoreCase(s)) {
            return getContentType();
        }

        String name = b.request.getHeader(s);
        if (name == null) {
            if (b.headers.get(s) != null) {
                return b.headers.get(s);
            }

            if (s.startsWith(X_ATMOSPHERE) && isNotNoOps()) {
                name = (String) b.request.getAttribute(s);
            }
        }

        if (name == null && checkCase) {
            return getHeader(s.toLowerCase(), false);
        }

        if (name == null && "connection".equalsIgnoreCase(s)) {
            return "keep-alive";
        }

        return name;
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public String getParameter(String s) {
        String name = isNotNoOps() ? b.request.getParameter(s) : null;
        if (name == null) {
            if (b.queryStrings.get(s) != null) {
                return b.queryStrings.get(s)[0];
            }
        }
        return name;
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public Map<String, String[]> getParameterMap() {
        if (!queryComputed) {
            queryComputed = true;
            Map<String, String[]> m = (isNotNoOps() ? b.request.getParameterMap() : Collections.<String, String[]>emptyMap());
            for (String e : m.keySet()) {
                b.queryStrings.put(e, getParameterValues(e));
            }
        }
        return Collections.unmodifiableMap(b.queryStrings);
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public Enumeration<String> getParameterNames() {
        return Collections.enumeration(getParameterMap().keySet());
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public String[] getParameterValues(String s) {
        String[] list = b.request.getParameterValues(s);
        if (list != null && b.queryStrings.get(s) != null) {
            String[] newList = b.queryStrings.get(s);
            if (!Arrays.deepEquals(list, newList)) {
                String[] s1 = new String[list.length + newList.length];
                System.arraycopy(list, 0, s1, 0, list.length);
                System.arraycopy(newList, 0, s1, list.length, newList.length);
                return s1;
            } else {
                return list;
            }
        } else {
            return list == null ? b.queryStrings.get(s) : list;
        }
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public String getProtocol() {
        return b.request.getProtocol();
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public ServletInputStream getInputStream() throws IOException {
        return bis == null ? (isNotNoOps() ? b.request.getInputStream() : null) : bis;
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public BufferedReader getReader() throws IOException {
        return br == null ? (isNotNoOps() ? b.request.getReader() : null) : br;
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public String getRealPath(String path) {
        return b.request.getRealPath(path);
    }

    /**
     * Add all headers contained with the Map.
     *
     * @param headers
     * @return this;
     */
    public AtmosphereRequest headers(Map<String, String> headers) {
        b.headers.putAll(headers);
        return this;
    }

    /**
     * Add a header.
     *
     * @param name
     * @param value
     * @return this
     */
    public AtmosphereRequest header(String name, String value) {
        b.headers.put(name, value);
        return this;
    }

    /**
     * Set the query string
     *
     * @param queryString
     * @return this
     */
    public AtmosphereRequest queryString(String queryString) {
        // Don't override the builder
        if (!queryString.isEmpty()) {
            b.queryString = queryString;
            QueryStringDecoder decoder = new QueryStringDecoder(getRequestURI() + "?" + queryString);
            Map<String, List<String>> m = decoder.getParameters();
            Map<String, String[]> newM = new HashMap<String, String[]>();
            for (Map.Entry<String, List<String>> q : m.entrySet()) {
                newM.put(q.getKey(), q.getValue().toArray(new String[