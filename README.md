### Description

This is a simple project for serving job applications to different potential employers.

Job applications are accessed using an encrypted key in the url, so employers can't access application not intended for them (unless they know the secret URL).

Most of its functionality is accomplished by ``inlines``.

Users can build different ``Applications``, each composed of reusable ``ApplicationPages``.

Using inlines, it's possibile to define snippets of common text that can be reused across pages and applications.

The following inlines are defined:
  * a generic ``GenericTitle``, which is composed of just a ``TextField``
  * ``WorkExperience``
  * ``Study``
  * ``Reference``
  * ``Skill``
  * ``Link``

### License

MIT License. See LICENSE file.
