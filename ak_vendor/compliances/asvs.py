from gettext import gettext as _

# Reference: https://github.com/OWASP/ASVS/tree/v4.0.2/4.0/en
data = [
    {
        "code": "V1.1.1",
        "id": "ASVS_1_1_1",
        "title": _(
            "Verify the use of a secure software development lifecycle "
            "that addresses security in all stages of development."
        ),
        "active": True,
    },
    {
        "code": "V1.1.2",
        "id": "ASVS_1_1_2",
        "title": _(
            "Verify the use of threat modeling for every design change or "
            "sprint planning to identify threats, plan for "
            "countermeasures, facilitate appropriate risk responses, and "
            "guide security testing."
        ),
        "active": True,
    },
    {
        "code": "V1.1.3",
        "id": "ASVS_1_1_3",
        "title": _(
            "Verify that all user stories and features contain functional "
            'security constraints, such as "As a user, I should be able '
            "to view and edit my profile. I should not be able to view or "
            "edit anyone else's profile\""
        ),
        "active": True,
    },
    {
        "code": "V1.1.4",
        "id": "ASVS_1_1_4",
        "title": _(
            "Verify documentation and justification of all the "
            "application's trust boundaries, components, and significant "
            "data flows."
        ),
        "active": True,
    },
    {
        "code": "V1.1.5",
        "id": "ASVS_1_1_5",
        "title": _(
            "Verify definition and security analysis of the application's "
            "high-level architecture and all connected remote services."
        ),
        "active": True,
    },
    {
        "code": "V1.1.6",
        "id": "ASVS_1_1_6",
        "title": _(
            "Verify implementation of centralized, simple (economy of "
            "design), vetted, secure, and reusable security controls to "
            "avoid duplicate, missing, ineffective, or insecure controls."
        ),
        "active": True,
    },
    {
        "code": "V1.1.7",
        "id": "ASVS_1_1_7",
        "title": _(
            "Verify availability of a secure coding checklist, security "
            "requirements, guideline, or policy to all developers and "
            "testers."
        ),
        "active": True,
    },
    {
        "code": "V1.10.1",
        "id": "ASVS_1_10_1",
        "title": _(
            "Verify that a source code control system is in use, with "
            "procedures to ensure that check-ins are accompanied by issues "
            "or change tickets. The source code control system should have "
            "access control and identifiable users to allow traceability "
            "of any changes."
        ),
        "active": True,
    },
    {
        "code": "V1.11.1",
        "id": "ASVS_1_11_1",
        "title": _(
            "Verify the definition and documentation of all application "
            "components in terms of the business or security functions "
            "they provide."
        ),
        "active": True,
    },
    {
        "code": "V1.11.2",
        "id": "ASVS_1_11_2",
        "title": _(
            "Verify that all high-value business logic flows, including "
            "authentication, session management and access control, do not "
            "share unsynchronized state."
        ),
        "active": True,
    },
    {
        "code": "V1.11.3",
        "id": "ASVS_1_11_3",
        "title": _(
            "Verify that all high-value business logic flows, including "
            "authentication, session management and access control are "
            "thread safe and resistant to time-of-check and time-of-use "
            "race conditions."
        ),
        "active": True,
    },
    {
        "code": "V1.12.1",
        "id": "ASVS_1_12_1",
        "title": _(
            "Verify that user-uploaded files are stored outside of the web root."
        ),
        "active": True,
    },
    {
        "code": "V1.12.2",
        "id": "ASVS_1_12_2",
        "title": _(
            "Verify that user-uploaded files - if required to be displayed "
            "or downloaded from the application - are served by either "
            "octet stream downloads, or from an unrelated domain, such as "
            "a cloud file storage bucket. Implement a suitable Content "
            "Security Policy (CSP) to reduce the risk from XSS vectors or "
            "other attacks from the uploaded file."
        ),
        "active": True,
    },
    {
        "code": "V1.14.1",
        "id": "ASVS_1_14_1",
        "title": _(
            "Verify the segregation of components of differing trust "
            "levels through well-defined security controls, firewall "
            "rules, API gateways, reverse proxies, cloud-based security "
            "groups, or similar mechanisms."
        ),
        "active": True,
    },
    {
        "code": "V1.14.2",
        "id": "ASVS_1_14_2",
        "title": _(
            "Verify that binary signatures, trusted connections, and "
            "verified endpoints are used to deploy binaries to remote "
            "devices."
        ),
        "active": True,
    },
    {
        "code": "V1.14.3",
        "id": "ASVS_1_14_3",
        "title": _(
            "Verify that the build pipeline warns of out-of-date or "
            "insecure components and takes appropriate actions."
        ),
        "active": True,
    },
    {
        "code": "V1.14.4",
        "id": "ASVS_1_14_4",
        "title": _(
            "Verify that the build pipeline contains a build step to "
            "automatically build and verify the secure deployment of the "
            "application, particularly if the application infrastructure "
            "is software defined, such as cloud environment build scripts."
        ),
        "active": True,
    },
    {
        "code": "V1.14.5",
        "id": "ASVS_1_14_5",
        "title": _(
            "Verify that application deployments adequately sandbox, "
            "containerize and/or isolate at the network level to delay and "
            "deter attackers from attacking other applications, especially "
            "when they are performing sensitive or dangerous actions such "
            "as deserialization."
        ),
        "active": True,
    },
    {
        "code": "V1.14.6",
        "id": "ASVS_1_14_6",
        "title": _(
            "Verify the application does not use unsupported, insecure, or "
            "deprecated client-side technologies such as NSAPI plugins, "
            "Flash, Shockwave, ActiveX, Silverlight, NACL, or client-side "
            "Java applets."
        ),
        "active": True,
    },
    {
        "code": "V1.2.1",
        "id": "ASVS_1_2_1",
        "title": _(
            "Verify the use of unique or special low-privilege operating "
            "system accounts for all application components, services, and "
            "servers."
        ),
        "active": True,
    },
    {
        "code": "V1.2.2",
        "id": "ASVS_1_2_2",
        "title": _(
            "Verify that communications between application components, "
            "including APIs, middleware and data layers, are "
            "authenticated. Components should have the least necessary "
            "privileges needed."
        ),
        "active": True,
    },
    {
        "code": "V1.2.3",
        "id": "ASVS_1_2_3",
        "title": _(
            "Verify that the application uses a single vetted "
            "authentication mechanism that is known to be secure, can be "
            "extended to include strong authentication, and has "
            "sufficient logging and monitoring to detect account abuse or "
            "breaches."
        ),
        "active": True,
    },
    {
        "code": "V1.2.4",
        "id": "ASVS_1_2_4",
        "title": _(
            "Verify that all authentication pathways and identity "
            "management APIs implement consistent authentication security "
            "control strength, such that there are no weaker alternatives "
            "per the risk of the application."
        ),
        "active": True,
    },
    {
        "code": "V1.4.1",
        "id": "ASVS_1_4_1",
        "title": _(
            "Verify that trusted enforcement points such as at access "
            "control gateways, servers, and serverless functions enforce "
            "access controls. Never enforce access controls on the client."
        ),
        "active": True,
    },
    {
        "code": "V1.4.2",
        "id": "ASVS_1_4_2",
        "title": _(
            "Verify that the chosen access control solution is flexible "
            "enough to meet the application's needs. "
        ),
        "active": True,
    },
    {
        "code": "V1.4.3",
        "id": "ASVS_1_4_3",
        "title": _(
            "Verify enforcement of the principle of least privilege in "
            "functions, data files, URLs, controllers, services, and other "
            "resources. This implies protection against spoofing and "
            "elevation of privilege."
        ),
        "active": True,
    },
    {
        "code": "V1.4.4",
        "id": "ASVS_1_4_4",
        "title": _(
            "Verify the application uses a single and well-vetted access "
            "control mechanism for accessing protected data and resources. "
            "All requests must pass through this single mechanism to avoid "
            "copy and paste or insecure alternative paths."
        ),
        "active": True,
    },
    {
        "code": "V1.4.5",
        "id": "ASVS_1_4_5",
        "title": _(
            "Verify that attribute or feature-based access control is used "
            "whereby the code checks the user's authorization for a "
            "feature/data item rather than just their role. Permissions "
            "should still be allocated using roles."
        ),
        "active": True,
    },
    {
        "code": "V1.5.1",
        "id": "ASVS_1_5_1",
        "title": _(
            "Verify that input and output requirements clearly define how "
            "to handle and process data based on type, content, and "
            "applicable laws, regulations, and other policy compliance."
        ),
        "active": True,
    },
    {
        "code": "V1.5.2",
        "id": "ASVS_1_5_2",
        "title": _(
            "Verify that serialization is not used when communicating with "
            "untrusted clients. If this is not possible, ensure that "
            "adequate integrity controls (and possibly encryption if "
            "sensitive data is sent) are enforced to prevent "
            "deserialization attacks including object injection."
        ),
        "active": True,
    },
    {
        "code": "V1.5.3",
        "id": "ASVS_1_5_3",
        "title": _(
            "Verify that input validation is enforced on a trusted service layer."
        ),
        "active": True,
    },
    {
        "code": "V1.5.4",
        "id": "ASVS_1_5_4",
        "title": _(
            "Verify that output encoding occurs close to or by the "
            "interpreter for which it is intended."
        ),
        "active": True,
    },
    {
        "code": "V1.6.1",
        "id": "ASVS_1_6_1",
        "title": _(
            "Verify that there is an explicit policy for management of "
            "cryptographic keys and that a cryptographic key lifecycle "
            "follows a key management standard such as NIST SP 800-57."
        ),
        "active": True,
    },
    {
        "code": "V1.6.2",
        "id": "ASVS_1_6_2",
        "title": _(
            "Verify that consumers of cryptographic services protect key "
            "material and other secrets by using key vaults or API based "
            "alternatives."
        ),
        "active": True,
    },
    {
        "code": "V1.6.3",
        "id": "ASVS_1_6_3",
        "title": _(
            "Verify that all keys and passwords are replaceable and are "
            "part of a well-defined process to re-encrypt sensitive data."
        ),
        "active": True,
    },
    {
        "code": "V1.6.4",
        "id": "ASVS_1_6_4",
        "title": _(
            "Verify that the architecture treats client-side secrets--such "
            "as symmetric keys, passwords, or API tokens--as insecure and "
            "never uses them to protect or access sensitive data."
        ),
        "active": True,
    },
    {
        "code": "V1.7.1",
        "id": "ASVS_1_7_1",
        "title": _(
            "Verify that a common logging format and approach is used "
            "across the system."
        ),
        "active": True,
    },
    {
        "code": "V1.7.2",
        "id": "ASVS_1_7_2",
        "title": _(
            "Verify that logs are securely transmitted to a preferably "
            "remote system for analysis, detection, alerting, and "
            "escalation."
        ),
        "active": True,
    },
    {
        "code": "V1.8.1",
        "id": "ASVS_1_8_1",
        "title": _(
            "Verify that all sensitive data is identified and classified "
            "into protection levels."
        ),
        "active": True,
    },
    {
        "code": "V1.8.2",
        "id": "ASVS_1_8_2",
        "title": _(
            "Verify that all protection levels have an associated set of "
            "protection requirements, such as encryption requirements, "
            "integrity requirements, retention, privacy and other "
            "confidentiality requirements, and that these are applied in "
            "the architecture."
        ),
        "active": True,
    },
    {
        "code": "V1.9.1",
        "id": "ASVS_1_9_1",
        "title": _(
            "Verify the application encrypts communications between "
            "components, particularly when these components are in "
            "different containers, systems, sites, or cloud providers."
        ),
        "active": True,
    },
    {
        "code": "V1.9.2",
        "id": "ASVS_1_9_2",
        "title": _(
            "Verify that application components verify the authenticity of "
            "each side in a communication link to prevent "
            "person-in-the-middle attacks. For example, application "
            "components should validate TLS certificates and chains."
        ),
        "active": True,
    },
    {
        "code": "V10.1.1",
        "id": "ASVS_10_1_1",
        "title": _(
            "Verify that a code analysis tool is in use that can detect "
            "potentially malicious code, such as time functions, unsafe "
            "file operations and network connections."
        ),
        "active": True,
    },
    {
        "code": "V10.2.1",
        "id": "ASVS_10_2_1",
        "title": _(
            "Verify that the application source code and third party "
            "libraries do not contain unauthorized phone home or data "
            "collection capabilities. Where such functionality exists, "
            "obtain the user's permission for it to operate  before "
            "collecting any data."
        ),
        "active": True,
    },
    {
        "code": "V10.2.2",
        "id": "ASVS_10_2_2",
        "title": _(
            "Verify that the application does not ask for unnecessary or "
            "excessive permissions to privacy related features or sensors, "
            "such as contacts, cameras, microphones, or location."
        ),
        "active": True,
    },
    {
        "code": "V10.2.3",
        "id": "ASVS_10_2_3",
        "title": _(
            "Verify that the application source code and third party "
            "libraries do not contain back doors, such as hard-coded or "
            "additional undocumented accounts or keys, code obfuscation, "
            "undocumented binary blobs, rootkits, or anti-debugging, "
            "insecure debugging features, or otherwise out of date, "
            "insecure, or hidden functionality that could be used "
            "maliciously if discovered."
        ),
        "active": True,
    },
    {
        "code": "V10.2.4",
        "id": "ASVS_10_2_4",
        "title": _(
            "Verify that the application source code and third party "
            "libraries do not contain time bombs by searching for date and "
            "time related functions."
        ),
        "active": True,
    },
    {
        "code": "V10.2.5",
        "id": "ASVS_10_2_5",
        "title": _(
            "Verify that the application source code and third party "
            "libraries do not contain malicious code, such as salami "
            "attacks, logic bypasses, or logic bombs."
        ),
        "active": True,
    },
    {
        "code": "V10.2.6",
        "id": "ASVS_10_2_6",
        "title": _(
            "Verify that the application source code and third party "
            "libraries do not contain Easter eggs or any other potentially "
            "unwanted functionality."
        ),
        "active": True,
    },
    {
        "code": "V10.3.1",
        "id": "ASVS_10_3_1",
        "title": _(
            "Verify that if the application has a client or server "
            "auto-update feature, updates should be obtained over secure "
            "channels and digitally signed. The update code must validate "
            "the digital signature of the update before installing or "
            "executing the update."
        ),
        "active": True,
    },
    {
        "code": "V10.3.2",
        "id": "ASVS_10_3_2",
        "title": _(
            "Verify that the application employs integrity protections, "
            "such as code signing or subresource integrity. The "
            "application must not load or execute code from untrusted "
            "sources, such as loading includes, modules, plugins, code, "
            "or libraries from untrusted sources or the Internet."
        ),
        "active": True,
    },
    {
        "code": "V10.3.3",
        "id": "ASVS_10_3_3",
        "title": _(
            "Verify that the application has protection from subdomain "
            "takeovers if the application relies upon DNS entries or DNS "
            "subdomains, such as expired domain names, out of date DNS "
            "pointers or CNAMEs, expired projects at public source code "
            "repos, or transient cloud APIs, serverless functions, or "
            "storage buckets (*autogen-bucket-id*.cloud.example.com) or "
            "similar. Protections can include ensuring that DNS names used "
            "by applications are regularly checked for expiry or change."
        ),
        "active": True,
    },
    {
        "code": "V11.1.1",
        "id": "ASVS_11_1_1",
        "title": _(
            "Verify the application will only process business logic flows "
            "for the same user in sequential step order and without "
            "skipping steps."
        ),
        "active": True,
    },
    {
        "code": "V11.1.2",
        "id": "ASVS_11_1_2",
        "title": _(
            "Verify the application will only process business logic flows "
            "with all steps being processed in realistic human time, i.e. "
            "transactions are not submitted too quickly."
        ),
        "active": True,
    },
    {
        "code": "V11.1.3",
        "id": "ASVS_11_1_3",
        "title": _(
            "Verify the application has appropriate limits for specific "
            "business actions or transactions which are correctly enforced "
            "on a per user basis."
        ),
        "active": True,
    },
    {
        "code": "V11.1.4",
        "id": "ASVS_11_1_4",
        "title": _(
            "Verify the application has sufficient anti-automation "
            "controls to detect and protect against data exfiltration, "
            "excessive business logic requests, excessive file uploads or "
            "denial of service attacks."
        ),
        "active": True,
    },
    {
        "code": "V11.1.5",
        "id": "ASVS_11_1_5",
        "title": _(
            "Verify the application has business logic limits or "
            "validation to protect against likely business risks or "
            "threats, identified using threat modeling or similar "
            "methodologies."
        ),
        "active": True,
    },
    {
        "code": "V11.1.6",
        "id": "ASVS_11_1_6",
        "title": _(
            'Verify the application does not suffer from "Time Of Check '
            'to Time Of Use" (TOCTOU) issues or other race conditions for '
            "sensitive operations."
        ),
        "active": True,
    },
    {
        "code": "V11.1.7",
        "id": "ASVS_11_1_7",
        "title": _(
            "Verify the application monitors for unusual events or "
            "activity from a business logic perspective. For example, "
            "attempts to perform actions out of order or actions which a "
            "normal user would never attempt."
        ),
        "active": True,
    },
    {
        "code": "V11.1.8",
        "id": "ASVS_11_1_8",
        "title": _(
            "Verify the application has configurable alerting when "
            "automated attacks or unusual activity is detected."
        ),
        "active": True,
    },
    {
        "code": "V12.1.1",
        "id": "ASVS_12_1_1",
        "title": _(
            "Verify that the application will not accept large files that "
            "could fill up storage or cause a denial of service."
        ),
        "active": True,
    },
    {
        "code": "V12.1.2",
        "id": "ASVS_12_1_2",
        "title": _(
            'Verify that compressed files are checked for "zip bombs" - '
            "small input files that will decompress into huge files thus "
            "exhausting file storage limits."
        ),
        "active": True,
    },
    {
        "code": "V12.1.3",
        "id": "ASVS_12_1_3",
        "title": _(
            "Verify that a file size quota and maximum number of files per "
            "user is enforced to ensure that a single user cannot fill up "
            "the storage with too many files, or excessively large files."
        ),
        "active": True,
    },
    {
        "code": "V12.2.1",
        "id": "ASVS_12_2_1",
        "title": _(
            "Verify that files obtained from untrusted sources are "
            "validated to be of expected type based on the file's content."
        ),
        "active": True,
    },
    {
        "code": "V12.3.1",
        "id": "ASVS_12_3_1",
        "title": _(
            "Verify that user-submitted filename metadata is not used "
            "directly by system or framework filesystems and that a URL "
            "API is used to protect against path traversal."
        ),
        "active": True,
    },
    {
        "code": "V12.3.2",
        "id": "ASVS_12_3_2",
        "title": _(
            "Verify that user-submitted filename metadata is validated or "
            "ignored to prevent the disclosure, creation, updating or "
            "removal of local files (LFI)."
        ),
        "active": True,
    },
    {
        "code": "V12.3.3",
        "id": "ASVS_12_3_3",
        "title": _(
            "Verify that user-submitted filename metadata is validated or "
            "ignored to prevent the disclosure or execution of remote "
            "files via Remote File Inclusion (RFI) or Server-side Request "
            "Forgery (SSRF) attacks."
        ),
        "active": True,
    },
    {
        "code": "V12.3.4",
        "id": "ASVS_12_3_4",
        "title": _(
            "Verify that the application protects against Reflective File "
            "Download (RFD) by validating or ignoring user-submitted "
            "filenames in a JSON, JSONP, or URL parameter, the response "
            "Content-Type header should be set to text/plain, and the "
            "Content-Disposition header should have a fixed filename."
        ),
        "active": True,
    },
    {
        "code": "V12.3.5",
        "id": "ASVS_12_3_5",
        "title": _(
            "Verify that untrusted file metadata is not used directly with "
            "system API or libraries, to protect against OS command "
            "injection."
        ),
        "active": True,
    },
    {
        "code": "V12.3.6",
        "id": "ASVS_12_3_6",
        "title": _(
            "Verify that the application does not include and execute "
            "functionality from untrusted sources, such as unverified "
            "content distribution networks, JavaScript libraries, node npm "
            "libraries, or server-side DLLs."
        ),
        "active": True,
    },
    {
        "code": "V12.4.1",
        "id": "ASVS_12_4_1",
        "title": _(
            "Verify that files obtained from untrusted sources are stored "
            "outside the web root, with limited permissions, preferably "
            "with strong validation."
        ),
        "active": True,
    },
    {
        "code": "V12.4.2",
        "id": "ASVS_12_4_2",
        "title": _(
            "Verify that files obtained from untrusted sources are scanned "
            "by antivirus scanners to prevent upload of known malicious "
            "content."
        ),
        "active": True,
    },
    {
        "code": "V12.5.1",
        "id": "ASVS_12_5_1",
        "title": _(
            "Verify that the web tier is configured to serve only files "
            "with specific file extensions to prevent unintentional "
            "information and source code leakage. For example, backup "
            "files (e.g. .bak), temporary working files (e.g. .swp), "
            "compressed files (.zip, .tar.gz, etc) and other extensions "
            "commonly used by editors should be blocked unless required."
        ),
        "active": True,
    },
    {
        "code": "V12.5.2",
        "id": "ASVS_12_5_2",
        "title": _(
            "Verify that direct requests to uploaded files will never be "
            "executed as HTML/JavaScript content."
        ),
        "active": True,
    },
    {
        "code": "V12.6.1",
        "id": "ASVS_12_6_1",
        "title": _(
            "Verify that the web or application server is configured with "
            "an allow list of resources or systems to which the server can "
            "send requests or load data/files from."
        ),
        "active": True,
    },
    {
        "code": "V13.1.1",
        "id": "ASVS_13_1_1",
        "title": _(
            "Verify that all application components use the same encodings "
            "and parsers to avoid parsing attacks that exploit different "
            "URI or file parsing behavior that could be used in SSRF and "
            "RFI attacks."
        ),
        "active": True,
    },
    {
        "code": "V13.1.2",
        "id": "ASVS_13_1_2",
        "title": _(
            "Verify that access to administration and management functions "
            "is limited to authorized administrators."
        ),
        "active": True,
    },
    {
        "code": "V13.1.3",
        "id": "ASVS_13_1_3",
        "title": _(
            "Verify API URLs do not expose sensitive information, such as "
            "the API key, session tokens etc."
        ),
        "active": True,
    },
    {
        "code": "V13.1.4",
        "id": "ASVS_13_1_4",
        "title": _(
            "Verify that authorization decisions are made at both the URI, "
            "enforced by programmatic or declarative security at the "
            "controller or router, and at the resource level, enforced by "
            "model-based permissions."
        ),
        "active": True,
    },
    {
        "code": "V13.1.5",
        "id": "ASVS_13_1_5",
        "title": _(
            "Verify that requests containing unexpected or missing content "
            "types are rejected with appropriate headers (HTTP response "
            "status 406 Unacceptable or 415 Unsupported Media Type)."
        ),
        "active": True,
    },
    {
        "code": "V13.2.1",
        "id": "ASVS_13_2_1",
        "title": _(
            "Verify that enabled RESTful HTTP methods are a valid choice "
            "for the user or action, such as preventing normal users using "
            "DELETE or PUT on protected API or resources."
        ),
        "active": True,
    },
    {
        "code": "V13.2.2",
        "id": "ASVS_13_2_2",
        "title": _(
            "Verify that JSON schema validation is in place and verified "
            "before accepting input."
        ),
        "active": True,
    },
    {
        "code": "V13.2.3",
        "id": "ASVS_13_2_3",
        "title": _(
            "Verify that RESTful web services that utilize cookies are "
            "protected from Cross-Site Request Forgery via the use of at "
            "least one or more of the following: double submit cookie "
            "pattern, CSRF nonces, or Origin request header checks."
        ),
        "active": True,
    },
    {
        "code": "V13.2.4",
        "id": "ASVS_13_2_4",
        "title": _(
            "Verify that REST services have anti-automation controls to "
            "protect against excessive calls, especially if the API is "
            "unauthenticated."
        ),
        "active": True,
    },
    {
        "code": "V13.2.5",
        "id": "ASVS_13_2_5",
        "title": _(
            "Verify that REST services explicitly check the incoming "
            "Content-Type to be the expected one, such as application/xml "
            "or application/json."
        ),
        "active": True,
    },
    {
        "code": "V13.2.6",
        "id": "ASVS_13_2_6",
        "title": _(
            "Verify that the message headers and payload are trustworthy "
            "and not modified in transit. Requiring strong encryption for "
            "transport (TLS only) may be sufficient in many cases as it "
            "provides both confidentiality and integrity protection. "
            "Per-message digital signatures can provide additional "
            "assurance on top of the transport protections for "
            "high-security applications but bring with them additional "
            "complexity and risks to weigh against the benefits."
        ),
        "active": True,
    },
    {
        "code": "V13.3.1",
        "id": "ASVS_13_3_1",
        "title": _(
            "Verify that XSD schema validation takes place to ensure a "
            "properly formed XML document, followed by validation of each "
            "input field before any processing of that data takes place."
        ),
        "active": True,
    },
    {
        "code": "V13.3.2",
        "id": "ASVS_13_3_2",
        "title": _(
            "Verify that the message payload is signed using WS-Security "
            "to ensure reliable transport between client and service."
        ),
        "active": True,
    },
    {
        "code": "V13.4.1",
        "id": "ASVS_13_4_1",
        "title": _(
            "Verify that a query allow list or a combination of depth "
            "limiting and amount limiting is used to prevent GraphQL or "
            "data layer expression Denial of Service (DoS) as a result of "
            "expensive, nested queries. For more advanced scenarios, query "
            "cost analysis should be used."
        ),
        "active": True,
    },
    {
        "code": "V13.4.2",
        "id": "ASVS_13_4_2",
        "title": _(
            "Verify that GraphQL or other data layer authorization logic "
            "should be implemented at the business logic layer instead of "
            "the GraphQL layer."
        ),
        "active": True,
    },
    {
        "code": "V14.1.1",
        "id": "ASVS_14_1_1",
        "title": _(
            "Verify that the application build and deployment processes "
            "are performed in a secure and repeatable way, such as CI / CD "
            "automation, automated configuration management, and automated "
            "deployment scripts."
        ),
        "active": True,
    },
    {
        "code": "V14.1.2",
        "id": "ASVS_14_1_2",
        "title": _(
            "Verify that compiler flags are configured to enable all "
            "available buffer overflow protections and warnings, including "
            "stack randomization, data execution prevention, and to break "
            "the build if an unsafe pointer, memory, format string, "
            "integer, or string operations are found."
        ),
        "active": True,
    },
    {
        "code": "V14.1.3",
        "id": "ASVS_14_1_3",
        "title": _(
            "Verify that server configuration is hardened as per the "
            "recommendations of the application server and frameworks "
            "in use."
        ),
        "active": True,
    },
    {
        "code": "V14.1.4",
        "id": "ASVS_14_1_4",
        "title": _(
            "Verify that the application, configuration, and all "
            "dependencies can be re-deployed using automated deployment "
            "scripts, built from a documented and tested runbook in a "
            "reasonable time, or restored from backups in a timely "
            "fashion."
        ),
        "active": True,
    },
    {
        "code": "V14.1.5",
        "id": "ASVS_14_1_5",
        "title": _(
            "Verify that authorized administrators can verify the "
            "integrity of all security-relevant configurations to detect "
            "tampering."
        ),
        "active": True,
    },
    {
        "code": "V14.2.1",
        "id": "ASVS_14_2_1",
        "title": _(
            "Verify that all components are up to date, preferably using a "
            "dependency checker during build or compile time."
        ),
        "active": True,
    },
    {
        "code": "V14.2.2",
        "id": "ASVS_14_2_2",
        "title": _(
            "Verify that all unneeded features, documentation, samples, "
            "configurations are removed, such as sample applications, "
            "platform documentation, and default or example users."
        ),
        "active": True,
    },
    {
        "code": "V14.2.3",
        "id": "ASVS_14_2_3",
        "title": _(
            "Verify that if application assets, such as JavaScript "
            "libraries, CSS or web fonts, are hosted externally on a "
            "Content Delivery Network (CDN) or external provider, "
            "Subresource Integrity (SRI) is used to validate the integrity "
            "of the asset."
        ),
        "active": True,
    },
    {
        "code": "V14.2.4",
        "id": "ASVS_14_2_4",
        "title": _(
            "Verify that third party components come from pre-defined, "
            "trusted and continually maintained repositories."
        ),
        "active": True,
    },
    {
        "code": "V14.2.5",
        "id": "ASVS_14_2_5",
        "title": _(
            "Verify that an inventory catalog is maintained of all third "
            "party libraries in use."
        ),
        "active": True,
    },
    {
        "code": "V14.2.6",
        "id": "ASVS_14_2_6",
        "title": _(
            "Verify that the attack surface is reduced by sandboxing or "
            "encapsulating third party libraries to expose only the "
            "required behaviour into the application."
        ),
        "active": True,
    },
    {
        "code": "V14.3.1",
        "id": "ASVS_14_3_1",
        "title": _(
            "Verify that web or application server and framework error "
            "messages are configured to deliver user actionable, "
            "customized responses to eliminate any unintended security "
            "disclosures."
        ),
        "active": True,
    },
    {
        "code": "V14.3.2",
        "id": "ASVS_14_3_2",
        "title": _(
            "Verify that web or application server and application "
            "framework debug modes are disabled in production to eliminate "
            "debug features, developer consoles, and unintended security "
            "disclosures."
        ),
        "active": True,
    },
    {
        "code": "V14.3.3",
        "id": "ASVS_14_3_3",
        "title": _(
            "Verify that the HTTP headers or any part of the HTTP response "
            "do not expose detailed version information of system "
            "components."
        ),
        "active": True,
    },
    {
        "code": "V14.4.1",
        "id": "ASVS_14_4_1",
        "title": _(
            "Verify that every HTTP response contains a Content-Type "
            "header. text/*, */*+xml and application/xml content types "
            "should also specify a safe character set (e.g., UTF-8, "
            "ISO-8859-1)."
        ),
        "active": True,
    },
    {
        "code": "V14.4.2",
        "id": "ASVS_14_4_2",
        "title": _(
            "Verify that all API responses contain a Content-Disposition: "
            'attachment; filename="api.json" header (or other '
            "appropriate filename for the content type)."
        ),
        "active": True,
    },
    {
        "code": "V14.4.3",
        "id": "ASVS_14_4_3",
        "title": _(
            "Verify that a Content Security Policy (CSP) response header "
            "is in place that helps mitigate impact for XSS attacks like "
            "HTML, DOM, JSON, and JavaScript injection vulnerabilities."
        ),
        "active": True,
    },
    {
        "code": "V14.4.4",
        "id": "ASVS_14_4_4",
        "title": _(
            "Verify that all responses contain a X-Content-Type-Options: "
            "nosniff header."
        ),
        "active": True,
    },
    {
        "code": "V14.4.5",
        "id": "ASVS_14_4_5",
        "title": _(
            "Verify that a Strict-Transport-Security header is included on "
            "all responses and for all subdomains, such as "
            "Strict-Transport-Security: max-age=15724800; "
            "includeSubdomains."
        ),
        "active": True,
    },
    {
        "code": "V14.4.6",
        "id": "ASVS_14_4_6",
        "title": _(
            'Verify that a suitable "Referrer-Policy" header is '
            'included, such as "no-referrer" or "same-origin".'
        ),
        "active": True,
    },
    {
        "code": "V14.4.7",
        "id": "ASVS_14_4_7",
        "title": _(
            "Verify that the content of a web application cannot be "
            "embedded in a third-party site by default and that embedding "
            "of the exact resources is only allowed where necessary by "
            "using suitable Content-Security-Policy: frame-ancestors and "
            "X-Frame-Options response headers."
        ),
        "active": True,
    },
    {
        "code": "V14.5.1",
        "id": "ASVS_14_5_1",
        "title": _(
            "Verify that the application server only accepts the HTTP "
            "methods in use by the application/API, including pre-flight "
            "OPTIONS, and logs/alerts on any requests that are not valid "
            "for the application context."
        ),
        "active": True,
    },
    {
        "code": "V14.5.2",
        "id": "ASVS_14_5_2",
        "title": _(
            "Verify that the supplied Origin header is not used for "
            "authentication or access control decisions, as the Origin "
            "header can easily be changed by an attacker."
        ),
        "active": True,
    },
    {
        "code": "V14.5.3",
        "id": "ASVS_14_5_3",
        "title": _(
            "Verify that the Cross-Origin Resource Sharing (CORS) "
            "Access-Control-Allow-Origin header uses a strict allow list "
            "of trusted domains and subdomains to match against and does "
            'not support the "null" origin.'
        ),
        "active": True,
    },
    {
        "code": "V14.5.4",
        "id": "ASVS_14_5_4",
        "title": _(
            "Verify that HTTP headers added by a trusted proxy or SSO "
            "devices, such as a bearer token, are authenticated by the "
            "application."
        ),
        "active": True,
    },
    {
        "code": "V2.1.1",
        "id": "ASVS_2_1_1",
        "title": _(
            "Verify that user set passwords are at least 12 characters in "
            "length (after multiple spaces are combined)."
        ),
        "active": True,
    },
    {
        "code": "V2.1.10",
        "id": "ASVS_2_1_10",
        "title": _(
            "Verify that there are no periodic credential rotation or "
            "password history requirements."
        ),
        "active": True,
    },
    {
        "code": "V2.1.11",
        "id": "ASVS_2_1_11",
        "title": _(
            'Verify that "paste" functionality, browser password '
            "helpers, and external password managers are permitted."
        ),
        "active": True,
    },
    {
        "code": "V2.1.12",
        "id": "ASVS_2_1_12",
        "title": _(
            "Verify that the user can choose to either temporarily view "
            "the entire masked password, or temporarily view the last "
            "typed character of the password on platforms that do not have "
            "this as built-in functionality."
        ),
        "active": True,
    },
    {
        "code": "V2.1.2",
        "id": "ASVS_2_1_2",
        "title": _(
            "Verify that passwords 64 characters or longer are permitted "
            "but may be no longer than 128 characters."
        ),
        "active": True,
    },
    {
        "code": "V2.1.3",
        "id": "ASVS_2_1_3",
        "title": _(
            "Verify that password truncation is not performed. However, "
            "consecutive multiple spaces may be replaced by a single "
            "space."
        ),
        "active": True,
    },
    {
        "code": "V2.1.4",
        "id": "ASVS_2_1_4",
        "title": _(
            "Verify that any printable Unicode character, including "
            "language neutral characters such as spaces and Emojis are "
            "permitted in passwords."
        ),
        "active": True,
    },
    {
        "code": "V2.1.5",
        "id": "ASVS_2_1_5",
        "title": _("Verify users can change their password."),
        "active": True,
    },
    {
        "code": "V2.1.6",
        "id": "ASVS_2_1_6",
        "title": _(
            "Verify that password change functionality requires the user's "
            "current and new password."
        ),
        "active": True,
    },
    {
        "code": "V2.1.7",
        "id": "ASVS_2_1_7",
        "title": _(
            "Verify that passwords submitted during account registration, "
            "login, and password change are checked against a set of "
            "breached passwords either locally (such as the top 1,000 or "
            "10,000 most common passwords which match the system's "
            "password policy) or using an external API. If using an API a "
            "zero knowledge proof or other mechanism should be used to "
            "ensure that the plain text password is not sent or used in "
            "verifying the breach status of the password. If the password "
            "is breached, the application must require the user to set a "
            "new non-breached password."
        ),
        "active": True,
    },
    {
        "code": "V2.1.8",
        "id": "ASVS_2_1_8",
        "title": _(
            "Verify that a password strength meter is provided to help "
            "users set a stronger password."
        ),
        "active": True,
    },
    {
        "code": "V2.1.9",
        "id": "ASVS_2_1_9",
        "title": _(
            "Verify that there are no password composition rules limiting "
            "the type of characters permitted. There should be no "
            "requirement for upper or lower case or numbers or special "
            "characters."
        ),
        "active": True,
    },
    {
        "code": "V2.10.1",
        "id": "ASVS_2_10_1",
        "title": _(
            "Verify that intra-service secrets do not rely on unchanging "
            "credentials such as passwords, API keys or shared accounts "
            "with privileged access."
        ),
        "active": True,
    },
    {
        "code": "V2.10.2",
        "id": "ASVS_2_10_2",
        "title": _(
            "Verify that if passwords are required for service "
            "authentication, the service account used is not a default "
            "credential. (e.g. root/root or admin/admin are default in "
            "some services during installation)."
        ),
        "active": True,
    },
    {
        "code": "V2.10.3",
        "id": "ASVS_2_10_3",
        "title": _(
            "Verify that passwords are stored with sufficient protection "
            "to prevent offline recovery attacks, including local system "
            "access."
        ),
        "active": True,
    },
    {
        "code": "V2.10.4",
        "id": "ASVS_2_10_4",
        "title": _(
            "Verify passwords, integrations with databases and third-party "
            "systems, seeds and internal secrets, and API keys are managed "
            "securely and not included in the source code or stored within "
            "source code repositories. Such storage SHOULD resist offline "
            "attacks. The use of a secure software key store (L1), "
            "hardware TPM, or an HSM (L3) is recommended for password "
            "storage."
        ),
        "active": True,
    },
    {
        "code": "V2.2.1",
        "id": "ASVS_2_2_1",
        "title": _(
            "Verify that anti-automation controls are effective at "
            "mitigating breached credential testing, brute force, and "
            "account lockout attacks. Such controls include blocking the "
            "most common breached passwords, soft lockouts, rate limiting, "
            "CAPTCHA, ever increasing delays between attempts, IP address "
            "restrictions, or risk-based restrictions such as location, "
            "first login on a device, recent attempts to unlock the "
            "account, or similar. Verify that no more than 100 failed "
            "attempts per hour is possible on a single account."
        ),
        "active": True,
    },
    {
        "code": "V2.2.2",
        "id": "ASVS_2_2_2",
        "title": _(
            "Verify that the use of weak authenticators (such as SMS and "
            "email) is limited to secondary verification and transaction "
            "approval and not as a replacement for more secure "
            "authentication methods. Verify that stronger methods are "
            "offered before weak methods, users are aware of the risks, or "
            "that proper measures are in place to limit the risks of "
            "account compromise."
        ),
        "active": True,
    },
    {
        "code": "V2.2.3",
        "id": "ASVS_2_2_3",
        "title": _(
            "Verify that secure notifications are sent to users after "
            "updates to authentication details, such as credential resets, "
            "email or address changes, logging in from unknown or risky "
            "locations. The use of push notifications - rather than SMS or "
            "email - is preferred, but in the absence of push "
            "notifications, SMS or email is acceptable as long as no "
            "sensitive information is disclosed in the notification."
        ),
        "active": True,
    },
    {
        "code": "V2.2.4",
        "id": "ASVS_2_2_4",
        "title": _(
            "Verify impersonation resistance against phishing, such as the "
            "use of multi-factor authentication, cryptographic devices "
            "with intent (such as connected keys with a push to "
            "authenticate), or at higher AAL levels, client-side "
            "certificates."
        ),
        "active": True,
    },
    {
        "code": "V2.2.5",
        "id": "ASVS_2_2_5",
        "title": _(
            "Verify that where a Credential Service Provider (CSP) and the "
            "application verifying authentication are separated, mutually "
            "authenticated TLS is in place between the two endpoints."
        ),
        "active": True,
    },
    {
        "code": "V2.2.6",
        "id": "ASVS_2_2_6",
        "title": _(
            "Verify replay resistance through the mandated use of One-time "
            "Passwords (OTP) devices, cryptographic authenticators, or "
            "lookup codes."
        ),
        "active": True,
    },
    {
        "code": "V2.2.7",
        "id": "ASVS_2_2_7",
        "title": _(
            "Verify intent to authenticate by requiring the entry of an "
            "OTP token or user-initiated action such as a button press on "
            "a FIDO hardware key."
        ),
        "active": True,
    },
    {
        "code": "V2.3.1",
        "id": "ASVS_2_3_1",
        "title": _(
            "Verify system generated initial passwords or activation codes "
            "SHOULD be securely randomly generated, SHOULD be at least 6 "
            "characters long, and MAY contain letters and numbers, and "
            "expire after a short period of time. These initial secrets "
            "must not be permitted to become the long term password."
        ),
        "active": True,
    },
    {
        "code": "V2.3.2",
        "id": "ASVS_2_3_2",
        "title": _(
            "Verify that enrollment and use of subscriber-provided "
            "authentication devices are supported, such as a U2F or FIDO "
            "tokens."
        ),
        "active": True,
    },
    {
        "code": "V2.3.3",
        "id": "ASVS_2_3_3",
        "title": _(
            "Verify that renewal instructions are sent with sufficient "
            "time to renew time bound authenticators."
        ),
        "active": True,
    },
    {
        "code": "V2.4.1",
        "id": "ASVS_2_4_1",
        "title": _(
            "Verify that passwords are stored in a form that is resistant "
            "to offline attacks. Passwords SHALL be salted and hashed "
            "using an approved one-way key derivation or password hashing "
            "function. Key derivation and password hashing functions take "
            "a password, a salt, and a cost factor as inputs when "
            "generating a password hash."
        ),
        "active": True,
    },
    {
        "code": "V2.4.2",
        "id": "ASVS_2_4_2",
        "title": _(
            "Verify that the salt is at least 32 bits in length and be "
            "chosen arbitrarily to minimize salt value collisions among "
            "stored hashes. For each credential, a unique salt value and "
            "the resulting hash SHALL be stored."
        ),
        "active": True,
    },
    {
        "code": "V2.4.3",
        "id": "ASVS_2_4_3",
        "title": _(
            "Verify that if PBKDF2 is used, the iteration count SHOULD be "
            "as large as verification server performance will allow, "
            "typically at least 100,000 iterations."
        ),
        "active": True,
    },
    {
        "code": "V2.4.4",
        "id": "ASVS_2_4_4",
        "title": _(
            "Verify that if bcrypt is used, the work factor SHOULD be as "
            "large as verification server performance will allow, "
            "typically at least 13."
        ),
        "active": True,
    },
    {
        "code": "V2.4.5",
        "id": "ASVS_2_4_5",
        "title": _(
            "Verify that an additional iteration of a key derivation "
            "function is performed, using a salt value that is secret and "
            "known only to the verifier. Generate the salt value using an "
            "approved random bit generator [SP 800-90Ar1] and provide at "
            "least the minimum security strength specified in the latest "
            "revision of SP 800-131A. The secret salt value SHALL be "
            "stored separately from the hashed passwords (e.g., in a "
            "specialized device like a hardware security module)."
        ),
        "active": True,
    },
    {
        "code": "V2.5.1",
        "id": "ASVS_2_5_1",
        "title": _(
            "Verify that a system generated initial activation or recovery "
            "secret is not sent in clear text to the user."
        ),
        "active": True,
    },
    {
        "code": "V2.5.2",
        "id": "ASVS_2_5_2",
        "title": _(
            "Verify password hints or knowledge-based authentication "
            '(so-called "secret questions") are not present.'
        ),
        "active": True,
    },
    {
        "code": "V2.5.3",
        "id": "ASVS_2_5_3",
        "title": _(
            "Verify password credential recovery does not reveal the "
            "current password in any way."
        ),
        "active": True,
    },
    {
        "code": "V2.5.4",
        "id": "ASVS_2_5_4",
        "title": _(
            "Verify shared or default accounts are not present (e.g. "
            '"root", "admin", or "sa").'
        ),
        "active": True,
    },
    {
        "code": "V2.5.5",
        "id": "ASVS_2_5_5",
        "title": _(
            "Verify that if an authentication factor is changed or "
            "replaced, that the user is notified of this event."
        ),
        "active": True,
    },
    {
        "code": "V2.5.6",
        "id": "ASVS_2_5_6",
        "title": _(
            "Verify forgotten password, and other recovery paths use a "
            "secure recovery mechanism, such as time-based OTP (TOTP) or "
            "other soft token, mobile push, or another offline recovery "
            "mechanism."
        ),
        "active": True,
    },
    {
        "code": "V2.5.7",
        "id": "ASVS_2_5_7",
        "title": _(
            "Verify that if OTP or multi-factor authentication factors are "
            "lost, that evidence of identity proofing is performed at the "
            "same level as during enrollment."
        ),
        "active": True,
    },
    {
        "code": "V2.6.1",
        "id": "ASVS_2_6_1",
        "title": _("Verify that lookup secrets can be used only once."),
        "active": True,
    },
    {
        "code": "V2.6.2",
        "id": "ASVS_2_6_2",
        "title": _(
            "Verify that lookup secrets have sufficient randomness (112 "
            "bits of entropy), or if less than 112 bits of entropy, salted "
            "with a unique and random 32-bit salt and hashed with an "
            "approved one-way hash."
        ),
        "active": True,
    },
    {
        "code": "V2.6.3",
        "id": "ASVS_2_6_3",
        "title": _(
            "Verify that lookup secrets are resistant to offline attacks, "
            "such as predictable values."
        ),
        "active": True,
    },
    {
        "code": "V2.7.1",
        "id": "ASVS_2_7_1",
        "title": _(
            'Verify that clear text out of band (NIST "restricted") '
            "authenticators, such as SMS or PSTN, are not offered by "
            "default, and stronger alternatives such as push notifications "
            "are offered first."
        ),
        "active": True,
    },
    {
        "code": "V2.7.2",
        "id": "ASVS_2_7_2",
        "title": _(
            "Verify that the out of band verifier expires out of band "
            "authentication requests, codes, or tokens after 10 minutes."
        ),
        "active": True,
    },
    {
        "code": "V2.7.3",
        "id": "ASVS_2_7_3",
        "title": _(
            "Verify that the out of band verifier authentication requests, "
            "codes, or tokens are only usable once, and only for the "
            "original authentication request."
        ),
        "active": True,
    },
    {
        "code": "V2.7.4",
        "id": "ASVS_2_7_4",
        "title": _(
            "Verify that the out of band authenticator and verifier "
            "communicates over a secure independent channel."
        ),
        "active": True,
    },
    {
        "code": "V2.7.5",
        "id": "ASVS_2_7_5",
        "title": _(
            "Verify that the out of band verifier retains only a hashed "
            "version of the authentication code."
        ),
        "active": True,
    },
    {
        "code": "V2.7.6",
        "id": "ASVS_2_7_6",
        "title": _(
            "Verify that the initial authentication code is generated by a "
            "secure random number generator, containing at least 20 bits "
            "of entropy (typically a six digital random number is "
            "sufficient)."
        ),
        "active": True,
    },
    {
        "code": "V2.8.1",
        "id": "ASVS_2_8_1",
        "title": _(
            "Verify that time-based OTPs have a defined lifetime before expiring."
        ),
        "active": True,
    },
    {
        "code": "V2.8.2",
        "id": "ASVS_2_8_2",
        "title": _(
            "Verify that symmetric keys used to verify submitted OTPs are "
            "highly protected, such as by using a hardware security module "
            "or secure operating system based key storage."
        ),
        "active": True,
    },
    {
        "code": "V2.8.3",
        "id": "ASVS_2_8_3",
        "title": _(
            "Verify that approved cryptographic algorithms are used in the "
            "generation, seeding, and verification of OTPs."
        ),
        "active": True,
    },
    {
        "code": "V2.8.4",
        "id": "ASVS_2_8_4",
        "title": _(
            "Verify that time-based OTP can be used only once within the "
            "validity period."
        ),
        "active": True,
    },
    {
        "code": "V2.8.5",
        "id": "ASVS_2_8_5",
        "title": _(
            "Verify that if a time-based multi-factor OTP token is re-used "
            "during the validity period, it is logged and rejected with "
            "secure notifications being sent to the holder of the device."
        ),
        "active": True,
    },
    {
        "code": "V2.8.6",
        "id": "ASVS_2_8_6",
        "title": _(
            "Verify physical single-factor OTP generator can be revoked in "
            "case of theft or other loss. Ensure that revocation is "
            "immediately effective across logged in sessions, regardless "
            "of location."
        ),
        "active": True,
    },
    {
        "code": "V2.8.7",
        "id": "ASVS_2_8_7",
        "title": _(
            "Verify that biometric authenticators are limited to use only "
            "as secondary factors in conjunction with either something you "
            "have and something you know."
        ),
        "active": True,
    },
    {
        "code": "V2.9.1",
        "id": "ASVS_2_9_1",
        "title": _(
            "Verify that cryptographic keys used in verification are "
            "stored securely and protected against disclosure, such as "
            "using a Trusted Platform Module (TPM) or Hardware Security "
            "Module (HSM), or an OS service that can use this secure "
            "storage."
        ),
        "active": True,
    },
    {
        "code": "V2.9.2",
        "id": "ASVS_2_9_2",
        "title": _(
            "Verify that the challenge nonce is at least 64 bits in "
            "length, and statistically unique or unique over the lifetime "
            "of the cryptographic device."
        ),
        "active": True,
    },
    {
        "code": "V2.9.3",
        "id": "ASVS_2_9_3",
        "title": _(
            "Verify that approved cryptographic algorithms are used in the "
            "generation, seeding, and verification."
        ),
        "active": True,
    },
    {
        "code": "V3.1.1",
        "id": "ASVS_3_1_1",
        "title": _(
            "Verify the application never reveals session tokens in URL parameters."
        ),
        "active": True,
    },
    {
        "code": "V3.2.1",
        "id": "ASVS_3_2_1",
        "title": _(
            "Verify the application generates a new session token on user "
            "authentication."
        ),
        "active": True,
    },
    {
        "code": "V3.2.2",
        "id": "ASVS_3_2_2",
        "title": _("Verify that session tokens possess at least 64 bits of entropy."),
        "active": True,
    },
    {
        "code": "V3.2.3",
        "id": "ASVS_3_2_3",
        "title": _(
            "Verify the application only stores session tokens in the "
            "browser using secure methods such as appropriately secured "
            "cookies (see section 3.4) or HTML 5 session storage."
        ),
        "active": True,
    },
    {
        "code": "V3.2.4",
        "id": "ASVS_3_2_4",
        "title": _(
            "Verify that session token are generated using approved "
            "cryptographic algorithms."
        ),
        "active": True,
    },
    {
        "code": "V3.3.1",
        "id": "ASVS_3_3_1",
        "title": _(
            "Verify that logout and expiration invalidate the session "
            "token, such that the back button or a downstream relying "
            "party does not resume an authenticated session, including "
            "across relying parties."
        ),
        "active": True,
    },
    {
        "code": "V3.3.2",
        "id": "ASVS_3_3_2",
        "title": _(
            "If authenticators permit users to remain logged in, verify "
            "that re-authentication occurs periodically both when actively "
            "used or after an idle period."
        ),
        "active": True,
    },
    {
        "code": "V3.3.3",
        "id": "ASVS_3_3_3",
        "title": _(
            "Verify that the application gives the option to terminate all "
            "other active sessions after a successful password change "
            "(including change via password reset/recovery), and that this "
            "is effective across the application, federated login (if "
            "present), and any relying parties."
        ),
        "active": True,
    },
    {
        "code": "V3.3.4",
        "id": "ASVS_3_3_4",
        "title": _(
            "Verify that users are able to view and (having re-entered "
            "login credentials) log out of any or all currently active "
            "sessions and devices."
        ),
        "active": True,
    },
    {
        "code": "V3.4.1",
        "id": "ASVS_3_4_1",
        "title": _(
            "Verify that cookie-based session tokens have the 'Secure' "
            "attribute set."
        ),
        "active": True,
    },
    {
        "code": "V3.4.2",
        "id": "ASVS_3_4_2",
        "title": _(
            "Verify that cookie-based session tokens have the 'HttpOnly' "
            "attribute set."
        ),
        "active": True,
    },
    {
        "code": "V3.4.3",
        "id": "ASVS_3_4_3",
        "title": _(
            "Verify that cookie-based session tokens utilize the "
            "'SameSite' attribute to limit exposure to cross-site request "
            "forgery attacks."
        ),
        "active": True,
    },
    {
        "code": "V3.4.4",
        "id": "ASVS_3_4_4",
        "title": _(
            'Verify that cookie-based session tokens use "__Host-" '
            "prefix (see references) to provide session cookie "
            "confidentiality."
        ),
        "active": True,
    },
    {
        "code": "V3.4.5",
        "id": "ASVS_3_4_5",
        "title": _(
            "Verify that if the application is published under a domain "
            "name with other applications that set or use session cookies "
            "that might override or disclose the session cookies, set the "
            "path attribute in cookie-based session tokens using the most "
            "precise path possible."
        ),
        "active": True,
    },
    {
        "code": "V3.5.1",
        "id": "ASVS_3_5_1",
        "title": _(
            "Verify the application allows users to revoke OAuth tokens "
            "that form trust relationships with linked applications."
        ),
        "active": True,
    },
    {
        "code": "V3.5.2",
        "id": "ASVS_3_5_2",
        "title": _(
            "Verify the application uses session tokens rather than static "
            "API secrets and keys, except with legacy implementations."
        ),
        "active": True,
    },
    {
        "code": "V3.5.3",
        "id": "ASVS_3_5_3",
        "title": _(
            "Verify that stateless session tokens use digital signatures, "
            "encryption, and other countermeasures to protect against "
            "tampering, enveloping, replay, null cipher, and key "
            "substitution attacks."
        ),
        "active": True,
    },
    {
        "code": "V3.6.1",
        "id": "ASVS_3_6_1",
        "title": _(
            "Verify that relying parties specify the maximum "
            "authentication time to Credential Service Providers (CSPs) "
            "and that CSPs re-authenticate the subscriber if they haven't "
            "used a session within that period."
        ),
        "active": True,
    },
    {
        "code": "V3.6.2",
        "id": "ASVS_3_6_2",
        "title": _(
            "Verify that Credential Service Providers (CSPs) inform "
            "Relying Parties (RPs) of the last authentication event, to "
            "allow RPs to determine if they need to re-authenticate the "
            "user."
        ),
        "active": True,
    },
    {
        "code": "V3.7.1",
        "id": "ASVS_3_7_1",
        "title": _(
            "Verify the application ensures a full, valid login session or "
            "requires re-authentication or secondary verification before "
            "allowing any sensitive transactions or account modifications."
        ),
        "active": True,
    },
    {
        "code": "V4.1.1",
        "id": "ASVS_4_1_1",
        "title": _(
            "Verify that the application enforces access control rules on "
            "a trusted service layer, especially if client-side access "
            "control is present and could be bypassed."
        ),
        "active": True,
    },
    {
        "code": "V4.1.2",
        "id": "ASVS_4_1_2",
        "title": _(
            "Verify that all user and data attributes and policy "
            "information used by access controls cannot be manipulated by "
            "end users unless specifically authorized."
        ),
        "active": True,
    },
    {
        "code": "V4.1.3",
        "id": "ASVS_4_1_3",
        "title": _(
            "Verify that the principle of least privilege exists - users "
            "should only be able to access functions, data files, URLs, "
            "controllers, services, and other resources, for which they "
            "possess specific authorization. This implies protection "
            "against spoofing and elevation of privilege."
        ),
        "active": True,
    },
    {
        "code": "V4.1.4",
        "id": "ASVS_4_1_4",
        "title": _(
            "Verify that the principle of deny by default exists whereby "
            "new users/roles start with minimal or no permissions and "
            "users/roles do not receive access to new features until "
            "access is explicitly assigned."
        ),
        "active": True,
    },
    {
        "code": "V4.1.5",
        "id": "ASVS_4_1_5",
        "title": _(
            "Verify that access controls fail securely including when an "
            "exception occurs."
        ),
        "active": True,
    },
    {
        "code": "V4.2.1",
        "id": "ASVS_4_2_1",
        "title": _(
            "Verify that sensitive data and APIs are protected against "
            "Insecure Direct Object Reference (IDOR) attacks targeting "
            "creation, reading, updating and deletion of records, such as "
            "creating or updating someone else's record, viewing "
            "everyone's records, or deleting all records."
        ),
        "active": True,
    },
    {
        "code": "V4.2.2",
        "id": "ASVS_4_2_2",
        "title": _(
            "Verify that the application or framework enforces a strong "
            "anti-CSRF mechanism to protect authenticated functionality, "
            "and effective anti-automation or anti-CSRF protects "
            "unauthenticated functionality."
        ),
        "active": True,
    },
    {
        "code": "V4.3.1",
        "id": "ASVS_4_3_1",
        "title": _(
            "Verify administrative interfaces use appropriate multi-factor "
            "authentication to prevent unauthorized use."
        ),
        "active": True,
    },
    {
        "code": "V4.3.2",
        "id": "ASVS_4_3_2",
        "title": _(
            "Verify that directory browsing is disabled unless "
            "deliberately desired. Additionally, applications should not "
            "allow discovery or disclosure of file or directory metadata, "
            "such as Thumbs.db, .DS_Store, .git or .svn folders."
        ),
        "active": True,
    },
    {
        "code": "V4.3.3",
        "id": "ASVS_4_3_3",
        "title": _(
            "Verify the application has additional authorization (such as "
            "step up or adaptive authentication) for lower value systems, "
            "and / or segregation of duties for high value applications to "
            "enforce anti-fraud controls as per the risk of application "
            "and past fraud."
        ),
        "active": True,
    },
    {
        "code": "V5.1.1",
        "id": "ASVS_5_1_1",
        "title": _(
            "Verify that the application has defenses against HTTP "
            "parameter pollution attacks, particularly if the application "
            "framework makes no distinction about the source of request "
            "parameters (GET, POST, cookies, headers, or environment "
            "variables)."
        ),
        "active": True,
    },
    {
        "code": "V5.1.2",
        "id": "ASVS_5_1_2",
        "title": _(
            "Verify that frameworks protect against mass parameter "
            "assignment attacks, or that the application has "
            "countermeasures to protect against unsafe parameter "
            "assignment, such as marking fields private or similar."
        ),
        "active": True,
    },
    {
        "code": "V5.1.3",
        "id": "ASVS_5_1_3",
        "title": _(
            "Verify that all input (HTML form fields, REST requests, URL "
            "parameters, HTTP headers, cookies, batch files, RSS feeds, "
            "etc) is validated using positive validation (allow lists)."
        ),
        "active": True,
    },
    {
        "code": "V5.1.4",
        "id": "ASVS_5_1_4",
        "title": _(
            "Verify that structured data is strongly typed and validated "
            "against a defined schema including allowed characters, length "
            "and pattern (e.g. credit card numbers or telephone, or "
            "validating that two related fields are reasonable, such as "
            "checking that suburb and zip/postcode match)."
        ),
        "active": True,
    },
    {
        "code": "V5.1.5",
        "id": "ASVS_5_1_5",
        "title": _(
            "Verify that URL redirects and forwards only allow "
            "destinations which appear on an allow list, or show a warning "
            "when redirecting to potentially untrusted content."
        ),
        "active": True,
    },
    {
        "code": "V5.2.1",
        "id": "ASVS_5_2_1",
        "title": _(
            "Verify that all untrusted HTML input from WYSIWYG editors or "
            "similar is properly sanitized with an HTML sanitizer library "
            "or framework feature."
        ),
        "active": True,
    },
    {
        "code": "V5.2.2",
        "id": "ASVS_5_2_2",
        "title": _(
            "Verify that unstructured data is sanitized to enforce safety "
            "measures such as allowed characters and length."
        ),
        "active": True,
    },
    {
        "code": "V5.2.3",
        "id": "ASVS_5_2_3",
        "title": _(
            "Verify that the application sanitizes user input before "
            "passing to mail systems to protect against SMTP or IMAP "
            "injection."
        ),
        "active": True,
    },
    {
        "code": "V5.2.4",
        "id": "ASVS_5_2_4",
        "title": _(
            "Verify that the application avoids the use of eval() or other "
            "dynamic code execution features. Where there is no "
            "alternative, any user input being included must be sanitized "
            "or sandboxed before being executed."
        ),
        "active": True,
    },
    {
        "code": "V5.2.5",
        "id": "ASVS_5_2_5",
        "title": _(
            "Verify that the application protects against template "
            "injection attacks by ensuring that any user input being "
            "included is sanitized or sandboxed."
        ),
        "active": True,
    },
    {
        "code": "V5.2.6",
        "id": "ASVS_5_2_6",
        "title": _(
            "Verify that the application protects against SSRF attacks, by "
            "validating or sanitizing untrusted data or HTTP file "
            "metadata, such as filenames and URL input fields, and uses "
            "allow lists of protocols, domains, paths and ports."
        ),
        "active": True,
    },
    {
        "code": "V5.2.7",
        "id": "ASVS_5_2_7",
        "title": _(
            "Verify that the application sanitizes, disables, or sandboxes "
            "user-supplied Scalable Vector Graphics (SVG) scriptable "
            "content, especially as they relate to XSS resulting from "
            "inline scripts, and foreignObject."
        ),
        "active": True,
    },
    {
        "code": "V5.2.8",
        "id": "ASVS_5_2_8",
        "title": _(
            "Verify that the application sanitizes, disables, or sandboxes "
            "user-supplied scriptable or expression template language "
            "content, such as Markdown, CSS or XSL stylesheets, BBCode, "
            "or similar."
        ),
        "active": True,
    },
    {
        "code": "V5.3.1",
        "id": "ASVS_5_3_1",
        "title": _(
            "Verify that output encoding is relevant for the interpreter "
            "and context required. For example, use encoders specifically "
            "for HTML values, HTML attributes, JavaScript, URL parameters, "
            "HTTP headers, SMTP, and others as the context requires, "
            "especially from untrusted inputs (e.g. names with Unicode or "
            "apostrophes, such as ねこ or O'Hara)."
        ),
        "active": True,
    },
    {
        "code": "V5.3.10",
        "id": "ASVS_5_3_10",
        "title": _(
            "Verify that the application protects against XPath injection "
            "or XML injection attacks."
        ),
        "active": True,
    },
    {
        "code": "V5.3.2",
        "id": "ASVS_5_3_2",
        "title": _(
            "Verify that output encoding preserves the user's chosen "
            "character set and locale, such that any Unicode character "
            "point is valid and safely handled."
        ),
        "active": True,
    },
    {
        "code": "V5.3.3",
        "id": "ASVS_5_3.3",
        "title": _(
            "Verify that context-aware, preferably automated - or at "
            "worst, manual - output escaping protects against reflected, "
            "stored, and DOM based XSS."
        ),
        "active": True,
    },
    {
        "code": "V5.3.4",
        "id": "ASVS_5_3_4",
        "title": _(
            "Verify that data selection or database queries (e.g. SQL, "
            "HQL, ORM, NoSQL) use parameterized queries, ORMs, entity "
            "frameworks, or are otherwise protected from database "
            "injection attacks."
        ),
        "active": True,
    },
    {
        "code": "V5.3.5",
        "id": "ASVS_5_3_5",
        "title": _(
            "Verify that where parameterized or safer mechanisms are not "
            "present, context-specific output encoding is used to protect "
            "against injection attacks, such as the use of SQL escaping to "
            "protect against SQL injection."
        ),
        "active": True,
    },
    {
        "code": "V5.3.6",
        "id": "ASVS_5_3_6",
        "title": _(
            "Verify that the application protects against JavaScript or "
            "JSON injection attacks, including for eval attacks, remote "
            "JavaScript includes, Content Security Policy (CSP) bypasses, "
            "DOM XSS, and JavaScript expression evaluation."
        ),
        "active": True,
    },
    {
        "code": "V5.3.7",
        "id": "ASVS_5_3_7",
        "title": _(
            "Verify that the application protects against LDAP injection "
            "vulnerabilities, or that specific security controls to "
            "prevent LDAP injection have been implemented."
        ),
        "active": True,
    },
    {
        "code": "V5.3.8",
        "id": "ASVS_5_3_8",
        "title": _(
            "Verify that the application protects against OS command "
            "injection and that operating system calls use parameterized "
            "OS queries or use contextual command line output encoding."
        ),
        "active": True,
    },
    {
        "code": "V5.3.9",
        "id": "ASVS_5_3_9",
        "title": _(
            "Verify that the application protects against Local File "
            "Inclusion (LFI) or Remote File Inclusion (RFI) attacks."
        ),
        "active": True,
    },
    {
        "code": "V5.4.1",
        "id": "ASVS_5_4_1",
        "title": _(
            "Verify that the application uses memory-safe string, safer "
            "memory copy and pointer arithmetic to detect or prevent "
            "stack, buffer, or heap overflows."
        ),
        "active": True,
    },
    {
        "code": "V5.4.2",
        "id": "ASVS_5_4_2",
        "title": _(
            "Verify that format strings do not take potentially hostile "
            "input, and are constant."
        ),
        "active": True,
    },
    {
        "code": "V5.4.3",
        "id": "ASVS_5_4_3",
        "title": _(
            "Verify that sign, range, and input validation techniques are "
            "used to prevent integer overflows."
        ),
        "active": True,
    },
    {
        "code": "V5.5.1",
        "id": "ASVS_5_5_1",
        "title": _(
            "Verify that serialized objects use integrity checks or are "
            "encrypted to prevent hostile object creation or data "
            "tampering."
        ),
        "active": True,
    },
    {
        "code": "V5.5.2",
        "id": "ASVS_5_5_2",
        "title": _(
            "Verify that the application correctly restricts XML parsers "
            "to only use the most restrictive configuration possible and "
            "to ensure that unsafe features such as resolving external "
            "entities are disabled to prevent XML eXternal Entity (XXE) "
            "attacks."
        ),
        "active": True,
    },
    {
        "code": "V5.5.3",
        "id": "ASVS_5_5_3",
        "title": _(
            "Verify that deserialization of untrusted data is avoided or "
            "is protected in both custom code and third-party libraries "
            "(such as JSON, XML and YAML parsers). "
        ),
        "active": True,
    },
    {
        "code": "V5.5.4",
        "id": "ASVS_5_5_4",
        "title": _(
            "Verify that when parsing JSON in browsers or JavaScript-based "
            "backends, JSON.parse is used to parse the JSON document. Do "
            "not use eval() to parse JSON."
        ),
        "active": True,
    },
    {
        "code": "V6.1.1",
        "id": "ASVS_6_1_1",
        "title": _(
            "Verify that regulated private data is stored encrypted while "
            "at rest, such as Personally Identifiable Information (PII), "
            "sensitive personal information, or data assessed likely to be "
            "subject to EU's GDPR."
        ),
        "active": True,
    },
    {
        "code": "V6.1.2",
        "id": "ASVS_6_1_2",
        "title": _(
            "Verify that regulated health data is stored encrypted while "
            "at rest, such as medical records, medical device details, or "
            "de-anonymized research records."
        ),
        "active": True,
    },
    {
        "code": "V6.1.3",
        "id": "ASVS_6_1_3",
        "title": _(
            "Verify that regulated financial data is stored encrypted "
            "while at rest, such as financial accounts, defaults or credit "
            "history, tax records, pay history, beneficiaries, or "
            "de-anonymized market or research records."
        ),
        "active": True,
    },
    {
        "code": "V6.2.1",
        "id": "ASVS_6_2_1",
        "title": _(
            "Verify that all cryptographic modules fail securely, and "
            "errors are handled in a way that does not enable Padding "
            "Oracle attacks."
        ),
        "active": True,
    },
    {
        "code": "V6.2.2",
        "id": "ASVS_6_2_2",
        "title": _(
            "Verify that industry proven or government approved "
            "cryptographic algorithms, modes, and libraries are used, "
            "instead of custom coded cryptography."
        ),
        "active": True,
    },
    {
        "code": "V6.2.3",
        "id": "ASVS_6_2_3",
        "title": _(
            "Verify that encryption initialization vector, cipher "
            "configuration, and block modes are configured securely using "
            "the latest advice."
        ),
        "active": True,
    },
    {
        "code": "V6.2.4",
        "id": "ASVS_6_2_4",
        "title": _(
            "Verify that random number, encryption or hashing algorithms, "
            "key lengths, rounds, ciphers or modes, can be reconfigured, "
            "upgraded, or swapped at any time, to protect against "
            "cryptographic breaks."
        ),
        "active": True,
    },
    {
        "code": "V6.2.5",
        "id": "ASVS_6_2_5",
        "title": _(
            "Verify that known insecure block modes (i.e. ECB, etc.), "
            "padding modes (i.e. PKCS#1 v1.5, etc.), ciphers with small "
            "block sizes (i.e. Triple-DES, Blowfish, etc.), and weak "
            "hashing algorithms (i.e. MD5, SHA1, etc.) are not used unless "
            "required for backwards compatibility."
        ),
        "active": True,
    },
    {
        "code": "V6.2.6",
        "id": "ASVS_6_2_6",
        "title": _(
            "Verify that nonces, initialization vectors, and other single "
            "use numbers must not be used more than once with a given "
            "encryption key. The method of generation must be appropriate "
            "for the algorithm being used."
        ),
        "active": True,
    },
    {
        "code": "V6.2.7",
        "id": "ASVS_6_2_7",
        "title": _(
            "Verify that encrypted data is authenticated via signatures, "
            "authenticated cipher modes, or HMAC to ensure that ciphertext "
            "is not altered by an unauthorized party."
        ),
        "active": True,
    },
    {
        "code": "V6.2.8",
        "id": "ASVS_6_2_8",
        "title": _(
            "Verify that all cryptographic operations are constant-time, "
            "with no 'short-circuit' operations in comparisons, "
            "calculations, or returns, to avoid leaking information."
        ),
        "active": True,
    },
    {
        "code": "V6.3.1",
        "id": "ASVS_6_3_1",
        "title": _(
            "Verify that all random numbers, random file names, random "
            "GUIDs, and random strings are generated using the "
            "cryptographic module's approved cryptographically secure "
            "random number generator when these random values are intended "
            "to be not guessable by an attacker."
        ),
        "active": True,
    },
    {
        "code": "V6.3.2",
        "id": "ASVS_6_3_2",
        "title": _(
            "Verify that random GUIDs are created using the GUID v4 "
            "algorithm, and a Cryptographically-secure Pseudo-random "
            "Number Generator (CSPRNG). GUIDs created using other "
            "pseudo-random number generators may be predictable."
        ),
        "active": True,
    },
    {
        "code": "V6.3.3",
        "id": "ASVS_6_3_3",
        "title": _(
            "Verify that random numbers are created with proper entropy "
            "even when the application is under heavy load, or that the "
            "application degrades gracefully in such circumstances."
        ),
        "active": True,
    },
    {
        "code": "V6.4.1",
        "id": "ASVS_6_4_1",
        "title": _(
            "Verify that a secrets management solution such as a key vault "
            "is used to securely create, store, control access to and "
            "destroy secrets."
        ),
        "active": True,
    },
    {
        "code": "V6.4.2",
        "id": "ASVS_6_4_2",
        "title": _(
            "Verify that key material is not exposed to the application "
            "but instead uses an isolated security module like a vault for "
            "cryptographic operations."
        ),
        "active": True,
    },
    {
        "code": "V7.1.1",
        "id": "ASVS_7_1_1",
        "title": _(
            "Verify that the application does not log credentials or "
            "payment details. Session tokens should only be stored in logs "
            "in an irreversible, hashed form."
        ),
        "active": True,
    },
    {
        "code": "V7.1.2",
        "id": "ASVS_7_1_2",
        "title": _(
            "Verify that the application does not log other sensitive data "
            "as defined under local privacy laws or relevant security "
            "policy."
        ),
        "active": True,
    },
    {
        "code": "V7.1.3",
        "id": "ASVS_7_1_3",
        "title": _(
            "Verify that the application logs security relevant events "
            "including successful and failed authentication events, access "
            "control failures, deserialization failures and input "
            "validation failures."
        ),
        "active": True,
    },
    {
        "code": "V7.1.4",
        "id": "ASVS_7_1_4",
        "title": _(
            "Verify that each log event includes necessary information "
            "that would allow for a detailed investigation of the timeline "
            "when an event happens."
        ),
        "active": True,
    },
    {
        "code": "V7.2.1",
        "id": "ASVS_7_2_1",
        "title": _(
            "Verify that all authentication decisions are logged, without "
            "storing sensitive session tokens or passwords. This should "
            "include requests with relevant metadata needed for security "
            "investigations."
        ),
        "active": True,
    },
    {
        "code": "V7.2.2",
        "id": "ASVS_7_2_2",
        "title": _(
            "Verify that all access control decisions can be logged and "
            "all failed decisions are logged. This should include requests "
            "with relevant metadata needed for security investigations."
        ),
        "active": True,
    },
    {
        "code": "V7.3.1",
        "id": "ASVS_7_3_1",
        "title": _(
            "Verify that the application appropriately encodes "
            "user-supplied data to prevent log injection."
        ),
        "active": True,
    },
    {
        "code": "V7.3.2",
        "id": "ASVS_7_3_2",
        "title": _(
            "Verify that all events are protected from injection when "
            "viewed in log viewing software."
        ),
        "active": True,
    },
    {
        "code": "V7.3.3",
        "id": "ASVS_7_3_3",
        "title": _(
            "Verify that security logs are protected from unauthorized "
            "access and modification."
        ),
        "active": True,
    },
    {
        "code": "V7.3.4",
        "id": "ASVS_7_3_4",
        "title": _(
            "Verify that time sources are synchronized to the correct time "
            "and time zone. Strongly consider logging only in UTC if "
            "systems are global to assist with post-incident forensic "
            "analysis."
        ),
        "active": True,
    },
    {
        "code": "V7.4.1",
        "id": "ASVS_7_4_1",
        "title": _(
            "Verify that a generic message is shown when an unexpected or "
            "security sensitive error occurs, potentially with a unique ID "
            "which support personnel can use to investigate."
        ),
        "active": True,
    },
    {
        "code": "V7.4.2",
        "id": "ASVS_7_4_2",
        "title": _(
            "Verify that exception handling (or a functional equivalent) "
            "is used across the codebase to account for expected and "
            "unexpected error conditions."
        ),
        "active": True,
    },
    {
        "code": "V7.4.3",
        "id": "ASVS_7_4_3",
        "title": _(
            'Verify that a "last resort" error handler is defined which '
            "will catch all unhandled exceptions."
        ),
        "active": True,
    },
    {
        "code": "V8.1.1",
        "id": "ASVS_8_1_1",
        "title": _(
            "Verify the application protects sensitive data from being "
            "cached in server components such as load balancers and "
            "application caches."
        ),
        "active": True,
    },
    {
        "code": "V8.1.2",
        "id": "ASVS_8_1_2",
        "title": _(
            "Verify that all cached or temporary copies of sensitive data "
            "stored on the server are protected from unauthorized access "
            "or purged/invalidated after the authorized user accesses the "
            "sensitive data."
        ),
        "active": True,
    },
    {
        "code": "V8.1.3",
        "id": "ASVS_8_1_3",
        "title": _(
            "Verify the application minimizes the number of parameters in "
            "a request, such as hidden fields, Ajax variables, cookies and "
            "header values."
        ),
        "active": True,
    },
    {
        "code": "V8.1.4",
        "id": "ASVS_8_1_4",
        "title": _(
            "Verify the application can detect and alert on abnormal "
            "numbers of requests, such as by IP, user, total per hour or "
            "day, or whatever makes sense for the application."
        ),
        "active": True,
    },
    {
        "code": "V8.1.5",
        "id": "ASVS_8_1_5",
        "title": _(
            "Verify that regular backups of important data are performed "
            "and that test restoration of data is performed."
        ),
        "active": True,
    },
    {
        "code": "V8.1.6",
        "id": "ASVS_8_1_6",
        "title": _(
            "Verify that backups are stored securely to prevent data from "
            "being stolen or corrupted."
        ),
        "active": True,
    },
    {
        "code": "V8.2.1",
        "id": "ASVS_8_2_1",
        "title": _(
            "Verify the application sets sufficient anti-caching headers "
            "so that sensitive data is not cached in modern browsers."
        ),
        "active": True,
    },
    {
        "code": "V8.2.2",
        "id": "ASVS_8_2_2",
        "title": _(
            "Verify that data stored in browser storage (such as HTML5 "
            "local storage, session storage, IndexedDB, or cookies) does "
            "not contain sensitive data or PII."
        ),
        "active": True,
    },
    {
        "code": "V8.2.3",
        "id": "ASVS_8_2_3",
        "title": _(
            "Verify that authenticated data is cleared from client "
            "storage, such as the browser DOM, after the client or session "
            "is terminated."
        ),
        "active": True,
    },
    {
        "code": "V8.3.1",
        "id": "ASVS_8_3_1",
        "title": _(
            "Verify that sensitive data is sent to the server in the HTTP "
            "message body or headers, and that query string parameters "
            "from any HTTP verb do not contain sensitive data."
        ),
        "active": True,
    },
    {
        "code": "V8.3.2",
        "id": "ASVS_8_3_2",
        "title": _(
            "Verify that users have a method to remove or export their "
            "data on demand."
        ),
        "active": True,
    },
    {
        "code": "V8.3.3",
        "id": "ASVS_8_3_3",
        "title": _(
            "Verify that users are provided clear language regarding "
            "collection and use of supplied personal information and that "
            "users have provided opt-in consent for the use of that data "
            "before it is used in any way."
        ),
        "active": True,
    },
    {
        "code": "V8.3.4",
        "id": "ASVS_8_3_4",
        "title": _(
            "Verify that all sensitive data created and processed by the "
            "application has been identified, and ensure that a policy is "
            "in place on how to deal with sensitive data."
        ),
        "active": True,
    },
    {
        "code": "V8.3.5",
        "id": "ASVS_8_3_5",
        "title": _(
            "Verify accessing sensitive data is audited (without logging "
            "the sensitive data itself), if the data is collected under "
            "relevant data protection directives or where logging of "
            "access is required."
        ),
        "active": True,
    },
    {
        "code": "V8.3.6",
        "id": "ASVS_8_3_6",
        "title": _(
            "Verify that sensitive information contained in memory is "
            "overwritten as soon as it is no longer required to mitigate "
            "memory dumping attacks, using zeroes or random data."
        ),
        "active": True,
    },
    {
        "code": "V8.3.7",
        "id": "ASVS_8_3_7",
        "title": _(
            "Verify that sensitive or private information that is required "
            "to be encrypted, is encrypted using approved algorithms that "
            "provide both confidentiality and integrity."
        ),
        "active": True,
    },
    {
        "code": "V8.3.8",
        "id": "ASVS_8_3_8",
        "title": _(
            "Verify that sensitive personal information is subject to data "
            "retention classification, such that old or out of date data "
            "is deleted automatically, on a schedule, or as the situation "
            "requires."
        ),
        "active": True,
    },
    {
        "code": "V9.1.1",
        "id": "ASVS_9_1_1",
        "title": _(
            "Verify that secured TLS is used for all client connectivity, "
            "and does not fall back to insecure or unencrypted protocols."
        ),
        "active": True,
    },
    {
        "code": "V9.1.2",
        "id": "ASVS_9_1_2",
        "title": _(
            "Verify using online or up to date TLS testing tools that only "
            "strong algorithms, ciphers, and protocols are enabled, with "
            "the strongest algorithms and ciphers set as preferred."
        ),
        "active": True,
    },
    {
        "code": "V9.1.3",
        "id": "ASVS_9_1_3",
        "title": _(
            "Verify that old versions of SSL and TLS protocols, "
            "algorithms, ciphers, and configuration are disabled, such as "
            "SSLv2, SSLv3, or TLS 1.0 and TLS 1.1. The latest version of "
            "TLS should be the preferred cipher suite."
        ),
        "active": True,
    },
    {
        "code": "V9.2.1",
        "id": "ASVS_9_2_1",
        "title": _(
            "Verify that connections to and from the server use trusted "
            "TLS certificates. Where internally generated or self-signed "
            "certificates are used, the server must be configured to only "
            "trust specific internal CAs and specific self-signed "
            "certificates. All others should be rejected."
        ),
        "active": True,
    },
    {
        "code": "V9.2.2",
        "id": "ASVS_9_2_2",
        "title": _(
            "Verify that encrypted communications such as TLS is used for "
            "all inbound and outbound connections, including for "
            "management ports, monitoring, authentication, API, or web "
            "service calls, database, cloud, serverless, mainframe, "
            "external, and partner connections. The server must not fall "
            "back to insecure or unencrypted protocols."
        ),
        "active": True,
    },
    {
        "code": "V9.2.3",
        "id": "ASVS_9_2_3",
        "title": _(
            "Verify that all encrypted connections to external systems "
            "that involve sensitive information or functions are "
            "authenticated."
        ),
        "active": True,
    },
    {
        "code": "V9.2.4",
        "id": "ASVS_9_2_4",
        "title": _(
            "Verify that proper certification revocation, such as Online "
            "Certificate Status Protocol (OCSP) Stapling, is enabled and "
            "configured."
        ),
        "active": True,
    },
    {
        "code": "V9.2.5",
        "id": "ASVS_9_2_5",
        "title": _("Verify that backend TLS connection failures are logged."),
        "active": True,
    },
]


class ASVS:
    def __init__(self, id, code, title, active=True):
        self.pk = id
        self.id = id
        self.title = title
        self.code = code
        self.active = active

    def __str__(self):
        return "%s - %s - %s" % (self.id, self.code, self.title)

    def __repr__(self):
        return "<ASVS: %s>" % self.__str__()


ASVS_DATA = {d["id"]: ASVS(**d) for d in data}
