from youtube_search import YoutubeSearch

def searchYT(input,max_results=10):
    results = YoutubeSearch(input, max_results=max_results).to_dict()

    # Keywords that might indicate triggering content
    triggering_keywords = ['sad', 'dies by suicide', 'death by suicide', 'self-harm', 'triggering']

    # Filter out potentially triggering results
    filtered_results = []
    for result in results:
        title = result['title'].lower()
        # Check if any triggering keyword is in the title or description
        if not any(keyword in title  for keyword in triggering_keywords):
            filtered_results.append(result)

    links = []
    for v in filtered_results:
        links.append('https://www.youtube.com' + v['url_suffix'])
    
    return links

if __name__ == '__main__':
    print(searchYT(input='postpartum - i feel sad after giving birth'))