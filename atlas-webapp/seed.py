from app import create_app, db
from models import Exhibition, MediaStation, MediaType, Interaction, Visualization, MediaContent

app = create_app()

with app.app_context():
    db.create_all()
    
    # Create an exhibition
    exhibition = Exhibition(title="Art Expo", start_date="2024-01-01", end_date="2024-12-31", location="New York")
    db.session.add(exhibition)
    db.session.commit()

    # Create media types, interactions, and visualizations
    audio = MediaType(name="Audio")
    video = MediaType(name="Video")
    image = MediaType(name="Image")
    zoom = Interaction(name="Zoom")
    compare = Interaction(name="Compare")
    slider = Visualization(name="Slider")
    glyph = Visualization(name="Glyph")

    db.session.add_all([audio, video, image, zoom, compare, slider, glyph])
    db.session.commit()

    # Create the first media station
    mediastation1 = MediaStation(title="Station 1", image_url="image1.jpg", description="Description of Station 1", path_to_exec="/path/to/executable1", exhibition_id=exhibition.id)
    db.session.add(mediastation1)
    db.session.commit()

    # Create media content for the first media station with audio and video types
    media_content1 = MediaContent(mediastation_id=mediastation1.id)
    media_content1.media_types.extend([audio, video])
    media_content1.interactions.extend([zoom])
    media_content1.visualizations.extend([slider])

    db.session.add(media_content1)
    db.session.commit()

    # Create the second media station
    mediastation2 = MediaStation(title="Station 2", image_url="image2.jpg", description="Description of Station 2", path_to_exec="/path/to/executable2", exhibition_id=exhibition.id)
    db.session.add(mediastation2)
    db.session.commit()

    # Create media content for the second media station with audio and image types
    media_content2 = MediaContent(mediastation_id=mediastation2.id)
    media_content2.media_types.extend([audio, image])
    media_content2.interactions.extend([compare])
    media_content2.visualizations.extend([glyph])

    db.session.add(media_content2)
    db.session.commit()

    # Retrieve and print media contents for the first media station
    station1 = MediaStation.query.filter_by(title="Station 1").first()
    print(f"Media contents for {station1.title}:")
    for content in station1.media_contents:
        print(f"  Media Content ID: {content.id}")
        for media_type in content.media_types:
            print(f"    Media Type: {media_type.name}")
        for interaction in content.interactions:
            print(f"    Interaction: {interaction.name}")
        for visualization in content.visualizations:
            print(f"    Visualization: {visualization.name}")

    # Retrieve and print media contents for the second media station
    station2 = MediaStation.query.filter_by(title="Station 2").first()
    print(f"Media contents for {station2.title}:")
    for content in station2.media_contents:
        print(f"  Media Content ID: {content.id}")
        for media_type in content.media_types:
            print(f"    Media Type: {media_type.name}")
        for interaction in content.interactions:
            print(f"    Interaction: {interaction.name}")
        for visualization in content.visualizations:
            print(f"    Visualization: {visualization.name}")
