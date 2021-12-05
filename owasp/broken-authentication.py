# Registration
    # Password handling
    # MFA
    # Confirm  identity

# Login
    # MFA
    # Auth token 
    # Session length 
    # logging out

# Credntial recovery
    # Password reset

# Password handling
    # Never encrypt password
    # Hash the password with salt
    # Use Password based Key Derivative Function (PBKDF)

# Password studding/spraying/guessing

        # Password/Credential stuffing : Usage of correct username and password the attacker already has and now uses that ona number of other login portals
            # Attack
                # Website login page - intercept using burp suite
                # Submit a user name and password and intercept using burp intruder
                # In intruder, clear symobols, add the passwords in the payload and start the attack
                # Watch out for response payload file. The failed logins will almost have the same size
                # The successful login will have a different response payload size with sometimes HTTP 302 indicating user is authenticaed.
            # Defense
                # Unique password
                # rate limiting
                # MFA
        # Password spraying - use a number of usernames with few known passwords
        # Password guessing - Brute force passwrod
            # attack
                # Website login page - intercept using burp suite
                # Submit a user name and password and intercept using burp intruder
                # In intruder, clear symobols, add the passwords in the payload and start the attack
                # Watch out for response payload file. The failed logins will almost have the same size
                # The successful login will have a different response payload size with sometimes HTTP 302 indicating user is authenticaed.
            # defense
                # strong password
                # MFA
                # disallow commonly used password (now a NIST standard)