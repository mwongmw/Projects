import boto3
import datetime


def lambda_handler(event, context):
   ec = boto3.client('ec2', region_name='us-east-1')

# Stage0
    year = "2022"
    month = "6"
    day = "23"

    today = datetime.date.today()

    scheduled = datetime.date(int(year), int(month), int(day))

    if today > scheduled:
        ec.stop_instances(InstanceIds=['i-0e71e0fc9a5090dca'])
    else:
        ec.start_instances(InstanceIds=['i-0e71e0fc9a5090dca'])
        ec.create_tags(Resources=['i-0e71e0fc9a5090dca'], Tags=[{'Key': 'schedule-on-off', 'Value': 'False'}])

# Stage1
    year = "2022"
    month = "1"
    day = "1"

    today = datetime.date.today()

    scheduled = datetime.date(int(year), int(month), int(day))

    if today > scheduled:
        ec.stop_instances(InstanceIds=['i-04e2a00103af50c64'])
    else:
        ec.start_instances(InstanceIds=['i-04e2a00103af50c64'])
        ec.create_tags(Resources=['i-04e2a00103af50c64'], Tags=[{'Key': 'schedule-on-off', 'Value': 'False'}])

# Stage2
    year = "2022"
    month = "1"
    day = "1"

    today = datetime.date.today()

    scheduled = datetime.date(int(year), int(month), int(day))

    if today > scheduled:
        ec.stop_instances(InstanceIds=['i-098d5ad6c753fe31e'])
    else:
        ec.start_instances(InstanceIds=['i-098d5ad6c753fe31e'])
        ec.create_tags(Resources=['i-098d5ad6c753fe31e'], Tags=[{'Key': 'schedule-on-off', 'Value': 'False'}])

# Stage3
    year = "2022"
    month = "1"
    day = "1"

    today = datetime.date.today()

    scheduled = datetime.date(int(year), int(month), int(day))

    if today > scheduled:
        ec.stop_instances(InstanceIds=['i-0e1300b82b873eb8f'])
    else:
        ec.start_instances(InstanceIds=['i-0e1300b82b873eb8f'])
        ec.create_tags(Resources=['i-0e1300b82b873eb8f'], Tags=[{'Key': 'schedule-on-off', 'Value': 'False'}])

# Stage4
    year = "2022"
    month = "1"
    day = "1"

    today = datetime.date.today()

    scheduled = datetime.date(int(year), int(month), int(day))

    if today > scheduled:
        ec.stop_instances(InstanceIds=['i-09ac6a54e89e4ca15'])
    else:
        ec.start_instances(InstanceIds=['i-09ac6a54e89e4ca15'])
        ec.create_tags(Resources=['i-09ac6a54e89e4ca15'], Tags=[{'Key': 'schedule-on-off', 'Value': 'False'}])

# Stage5
    year = "2022"
    month = "1"
    day = "1"

    today = datetime.date.today()

    scheduled = datetime.date(int(year), int(month), int(day))

    if today > scheduled:
        ec.stop_instances(InstanceIds=['i-0eb996f0f6e40c7ea'])
    else:
        ec.start_instances(InstanceIds=['i-0eb996f0f6e40c7ea'])
        ec.create_tags(Resources=['i-0eb996f0f6e40c7ea'], Tags=[{'Key': 'schedule-on-off', 'Value': 'False'}])

# Stage6
    year = "2022"
    month = "1"
    day = "1"

    today = datetime.date.today()

    scheduled = datetime.date(int(year), int(month), int(day))

    if today > scheduled:
        ec.stop_instances(InstanceIds=['i-02da7ba46b2eb0ab6'])
    else:
        ec.start_instances(InstanceIds=['i-02da7ba46b2eb0ab6'])
        ec.create_tags(Resources=['i-02da7ba46b2eb0ab6'], Tags=[{'Key': 'schedule-on-off', 'Value': 'False'}])

# Stage7
    year = "2022"
    month = "1"
    day = "1"

    today = datetime.date.today()

    scheduled = datetime.date(int(year), int(month), int(day))

    if today > scheduled:
        ec.stop_instances(InstanceIds=['i-0b6e4379300511dec'])
    else:
        ec.start_instances(InstanceIds=['i-0b6e4379300511dec'])
        ec.create_tags(Resources=['i-0b6e4379300511dec'], Tags=[{'Key': 'schedule-on-off', 'Value': 'False'}])

# Stage8
    year = "2022"
    month = "1"
    day = "1"

    today = datetime.date.today()

    scheduled = datetime.date(int(year), int(month), int(day))

    if today > scheduled:
        ec.stop_instances(InstanceIds=['i-0f6dd162409c2d931'])
    else:
        ec.start_instances(InstanceIds=['i-0f6dd162409c2d931'])
        ec.create_tags(Resources=['i-0f6dd162409c2d931'], Tags=[{'Key': 'schedule-on-off', 'Value': 'False'}])

# Stage9
    year = "2022"
    month = "1"
    day = "1"

    today = datetime.date.today()

    scheduled = datetime.date(int(year), int(month), int(day))

    if today > scheduled:
        ec.stop_instances(InstanceIds=['i-0adbd95718b958db9'])
    else:
        ec.start_instances(InstanceIds=['i-0adbd95718b958db9'])
        ec.create_tags(Resources=['i-0adbd95718b958db9'], Tags=[{'Key': 'schedule-on-off', 'Value': 'False'}])

# Stage100
    year = "2022"
    month = "1"
    day = "1"

    today = datetime.date.today()

    scheduled = datetime.date(int(year), int(month), int(day))

    if today > scheduled:
        ec.stop_instances(InstanceIds=['i-0eb8379f3ca74f74b'])
    else:
        ec.start_instances(InstanceIds=['i-0eb8379f3ca74f74b'])
        ec.create_tags(Resources=['i-0eb8379f3ca74f74b'], Tags=[{'Key': 'schedule-on-off', 'Value': 'False'}])


# UAT1
    year = "2022"
    month = "1"
    day = "1"

    today = datetime.date.today()

    scheduled = datetime.date(int(year), int(month), int(day))

    if today > scheduled:
        ec.stop_instances(InstanceIds=['i-00179d125b16c1a0d'])
    else:
        ec.start_instances(InstanceIds=['i-00179d125b16c1a0d'])
        ec.create_tags(Resources=['i-00179d125b16c1a0d'], Tags=[{'Key': 'schedule-on-off', 'Value': 'False'}])
