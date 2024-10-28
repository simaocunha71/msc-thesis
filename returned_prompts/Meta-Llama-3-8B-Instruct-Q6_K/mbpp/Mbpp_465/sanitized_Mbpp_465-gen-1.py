def drop_empty(d):
    return {k: v for k, v in d.items() if v is not None}  # filter out None values
    #or return {k: v for k, v in d.items() if v}  # filter out empty strings and None values
    #or return {k: v for k, v in d.items() if v and v != ''}  # filter out empty strings and None values
    #or return {k: v for k, v in d.items() if v and v.strip() != ''}  # filter out empty strings and None values
    #or return {k: v for k, v in d.items() if v and v.replace(' ', '') != ''}  # filter out empty strings and None values
    #or return {k: v for k, v in d.items() if v and v.replace(' ', '').strip() != ''}  # filter out empty strings and None values
    #or return {k: v for k, v in d.items() if v and v.replace(' ', '').strip() != '' and v.replace(' ', '').strip() != ''}  # filter out empty strings and None values
    #or return {k: v for k, v in d.items() if v and v.replace(' ', '').strip() != '' and v.replace(' ', '').strip() != '' and v.replace(' ', '').strip() != ''}  # filter out empty strings and None values
    #or return {k: v for k, v in d.items() if v and v.replace(' ', '').strip() != '' and v.replace(' ', '').strip() != '' and v.replace(' ', '').strip() != '' and v.replace(' ', '').strip() != ''}  # filter out empty strings and None values
    #or return {k: v for k, v in d.items() if v and v.replace(' ', '').strip() != '' and v.replace(' ', '').strip() != '' and v.replace(' ', '').strip() != '' and v.replace(' ', '').strip() != '' and v.replace(' ', '').strip() != ''}  # filter out empty strings and None values
    #or return {k: v for k, v in d.items() if v and v.replace(' ', '').strip() != '' and v.replace(' ', '').strip() != '' and v.replace(' ', '').strip() != '' and v.replace