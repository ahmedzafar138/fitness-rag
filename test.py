from pinecone import Pinecone

pc = Pinecone(api_key='pcsk_6n6KGz_5WN4e8qCAScRZK6JbNN3eU8bPeCCKFaUVw4WfDegx4dsGchnYRSsqW1NgJ2jU89')

# List all indexes to see their host and region details
for index in pc.list_indexes():
    print(f"Index Name: {index.name}")
    print(f"Region: {index.spec.serverless.region if index.spec.serverless else index.spec.pod.environment}")
