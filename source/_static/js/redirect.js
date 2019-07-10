// Automatic HTTPS redirect for production environment.
//
// Original source from https://github.com/runwayml/model-sdk/pull/28
// Adapted with use of https://gist.github.com/fevangelou/82f2a516efd8c8a8b278
//
// Read the Docs doesn't currently support HTTPS redirects for CNAME domains
// This is a hacky work around that keeps us free of having to host our own
// server-side component.
if (!(window.location.host.startsWith("127.0.0.1") || window.location.host.startsWith("localhost")) && (location.protocol != 'https:')) {
  location.href = 'https:' + window.location.href.substring(window.location.protocol.length);
}
