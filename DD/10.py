def generate_prime_and_primitive_root():
    # Take user input for the prime number and primitive root
    q = int(input("Enter a prime number (q): "))
    alpha = int(input("Enter a primitive root modulo p (alpha): "))
    return q, alpha

def generate_keys(q, alpha, name):
    # Take user input for the private key
    private_key = int(input(f"Enter {name}'s private key: "))
    public_key = pow(alpha, private_key, q)   # Public key (g^private_key % p)
    return private_key, public_key

def compute_shared_secret(received_public_key, private_key, q):
    shared_secret = pow(received_public_key, private_key, q)
    return shared_secret

def diffie_hellman():
    q, alpha = generate_prime_and_primitive_root()
    print(f"\nPrime (alpha): {q}, Primitive Root (alpha): {alpha}")

    # Alice generates her keys
    alice_private, alice_public = generate_keys(q, alpha, "Alice")
    print(f"Alice's Private Key: {alice_private}, Alice's Public Key: {alice_public}")

    # Bob generates his keys
    bob_private, bob_public = generate_keys(q, alpha, "Bob")
    print(f"Bob's Private Key: {bob_private}, Bob's Public Key: {bob_public}")

    # Exchange public keys and compute shared secrets
    alice_shared_secret = compute_shared_secret(bob_public, alice_private, q)
    bob_shared_secret = compute_shared_secret(alice_public, bob_private, q)

    print(f"Alice's Shared Secret: {alice_shared_secret}")
    print(f"Bob's Shared Secret: {bob_shared_secret}")

    # Verify that both shared secrets are the same
    assert alice_shared_secret == bob_shared_secret, "Shared secrets do not match!"
    print("Shared secret established successfully!")

# Run the Diffie-Hellman key exchange simulation
diffie_hellman()

