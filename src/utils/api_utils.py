def generate_cover_letter(client, prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert career consultant and professional writer, who specializes in drafting cover letters."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=800,
        temperature=0.4,
    )
    return response.choices[0].message.content


