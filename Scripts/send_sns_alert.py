import json
import mysql.connector

sqs = boto3.client('sqs')
sns = boto3.client('sns')
queue_url = 'https://sqs.ap-south-1.amazonaws.com/008673239246/pizza-alert-queue-aahash'

# Connect to RDS (Replace with your config)
conn = mysql.connector.connect(
    host='pizzadb-aahash.c7ok6ko8wnwq.ap-south-1.rds.amazonaws.com',
    user='admin',
    password='Aahash123',
    database='pizza_db_aahash'
)
cursor = conn.cursor(dictionary=True)

def fetch_store_info(store_id):
    cursor.execute("SELECT store_id, store_email FROM store_manager WHERE store_id = %s", (store_id,))
    return cursor.fetchone()

def send_sns(email, message):
    sns.publish(
        TopicArn='arn:aws:sns:ap-south-1:008673239246:pizza_store_alerts-aahash:04e8b4d8-6fe3-4fae-a434-5504baefc579',
        Message=message,
        Subject='Inventory Alert'
    )

while True:
    messages = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=5, WaitTimeSeconds=10)
    if 'Messages' not in messages:
        continue
    for msg in messages['Messages']:
        body = json.loads(msg['Body'])
        store_info = fetch_store_info(body['store_id'])

        if store_info:
            alert = f"""
            Store ID: {store_info['store_id']}
            SKU: {body['sku_name']} ({body['sku_id']})
            Quantity: {body['quantity']}
            Action Required: Restock immediately!
            """
            send_sns(store_info['store_email'], alert)

        # Delete message from queue
        sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=msg['ReceiptHandle'])
