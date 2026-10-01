
# Cryptography & Network Security Project

## 1. Project Overview

This project demonstrates practical applications of cryptography and network security. It includes an encryption and decryption programme, an integrity verification function, a risk assessment, and a firewall access-control configuration.

The project was developed in an authorised laboratory environment for educational purposes.

---

## 2. Project Structure

```text
cryptography network security exam/
│
├── src/
│   └── [source code for the security programme]
│
├── security tool.py
│   └── Security-related Python programme
│
├── risk assessment.md
│   └── Assets, vulnerabilities, risk rankings and recommended controls
│
├── firewall.conf
│   └── Laboratory firewall configuration and access-control rules
│
├── filter_tests.md
│   └── Firewall test commands, expected outcomes and test results
│
├── README.md
│   └── Project documentation and instructions
│
├── report.tex
│   └── LaTeX source for the technical report
│
└── report.pdf
    └── Compiled PDF version of the technical report
```

---

## 3. Security Programme

The Python security programme demonstrates basic cryptographic security functions.

The programme includes:

* Encryption of information.
* Decryption of encrypted information.
* Integrity verification using a hash.
* Testing to verify that encrypted information can be recovered correctly.
* Integrity checking to identify whether information has been modified.

### Running the Programme

Open the project in Visual Studio Code and open the integrated terminal.

Navigate to the project directory if necessary and run the Python programme using:

```bash
python3 "security tool.py"
```

If the programme is located inside the `src` directory, use:

```bash
python3 src/"security tool.py"
```

Follow the instructions displayed by the programme.

---

## 4. Encryption and Decryption Tests

The encryption test verifies that plaintext can be converted into ciphertext.

The decryption test verifies that the ciphertext can be converted back into the original plaintext.

The expected process is:

```text
Plaintext
    |
    v
Encryption
    |
    v
Ciphertext
    |
    v
Decryption
    |
    v
Original Plaintext
```

A successful test should produce the original plaintext after decryption.

---

## 5. Integrity Test

The integrity function uses a cryptographic hash to verify whether information has been changed.

The process is:

```text
Original Data
     |
     v
Hash Function
     |
     v
Hash Value
```

If the original data is modified and hashed again, the resulting hash should be different.

This demonstrates how integrity verification can detect unauthorised modification of data.

---

## 6. Firewall Configuration

The firewall configuration is contained in:

```text
firewall.conf
```

The laboratory configuration uses the following network structure:

| Component                | Address         |
| ------------------------ | --------------- |
| Student Records Server   | 192.168.10.10   |
| Guest Network            | 192.168.20.0/24 |
| Authorised Staff Network | 192.168.30.0/24 |
| Protected Service        | SSH             |
| Port                     | 22/TCP          |

The firewall policy is:

1. Block guest network access to the Student Records Server.
2. Permit authorised staff network access to the SSH service.
3. Block other inbound access to the SSH service.
4. Drop other inbound traffic that has not been explicitly authorised.

---

## 7. Reproducing the Firewall Tests

The firewall test procedure is documented in:

```text
filter_tests.md
```

Three tests are included:

### Test 1 – Authorised Staff

The authorised staff network attempts to access SSH on the Student Records Server.

Expected result:

```text
Connection permitted.
```

### Test 2 – Guest Network

The guest network attempts to access the protected server.

Expected result:

```text
Connection blocked.
```

### Test 3 – Other Network

An unauthorised source attempts to access the protected SSH service.

Expected result:

```text
Connection blocked.
```

The test commands and results are documented in `filter_tests.md`.

> The firewall test results in this project are identified as simulated laboratory results because no specific network addresses or service were supplied by the assessor.

---

## 8. Risk Assessment

The file:

```text
risk assessment.md
```

contains the project's identified assets, vulnerabilities, risk rankings and recommended security controls.

The risk assessment is used to identify threats to the system and determine appropriate measures for reducing those risks.

---

## 9. Technical Report

The technical report is provided in two formats:

```text
report.tex
```

The LaTeX source file allows the report to be reproduced or edited.

```text
report.pdf
```

The PDF is the compiled version of the technical report for submission.

The report covers:

* Assets and vulnerabilities.
* Risk rankings and recommended controls.
* Encryption and decryption.
* Integrity verification.
* Firewall configuration.
* Firewall testing.
* Results and conclusion.
* GitHub repository information.

---

## 10. GitHub Submission

All project files are maintained in the GitHub repository.

The repository contains the source code, risk assessment, firewall configuration, firewall test evidence, README documentation and LaTeX technical report.

The repository URL is:

**[(https://github.com/fabuwase/cryptography-network-security-exam)]**

---

## 11. Conclusion

This project demonstrates the application of cryptographic and network-security techniques in an authorised laboratory environment. Encryption and decryption provide confidentiality, integrity verification helps identify unauthorised modification, and firewall rules provide network access control by allowing authorised connections while blocking unauthorised access.
