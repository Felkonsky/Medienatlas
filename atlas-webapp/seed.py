from app import create_app, db
from models import Exhibition, MediaStation, MediaType, Interaction, Visualization, MediaContent

app = create_app()

with app.app_context():
    db.create_all()
    
    # Create exhibition 01
    exhibition = Exhibition(title="Anselmi bis Zuccari. Meisterzeichnungen der Sammlung Hoesch zu Gast", start_date="10-06-2022", end_date="11.09.2022", location="Residenzschloss", trailer='Sammeln verbindet: Wer sammelt, bringt Dinge zusammen, genießt die unmittelbare Begegnung mit den eigenen Schätzen und kann die Freude mit Gleichgesinnten teilen. Getreu diesem Motto bietet das Kupferstich-Kabinett der Staatlichen Kunstsammlungen Dresden (SKD) mit der Ausstellung „Anselmi bis Zuccari. Meisterzeichnungen der Sammlung Hoesch zu Gast“ vom 10. Juni bis zum 11. September 2022 die Gelegenheit, hochkarätige sowie bisher kaum öffentlich gezeigte Altmeisterzeichnungen aus der Sammlung des Winzers und Historikers Dr. Henning Hoesch kennenzulernen. Ausgewählte Blätter aus dem eigenen Bestand gesellen sich zu den Zeichnungen aus der Sammlung Hoesch und regen neue Verbindungen an. Insgesamt sind 111 Werke ausgestellt, davon 79 Zeichnungen aus der Sammlung Hoesch, einem seit über vier Jahrzehnten mit Leidenschaft und einem kundigen Auge zusammengetragenem Bestand. Italienische Arbeiten auf Papier aus der Renaissance und dem Barock bilden den Schwerpunkt und zeugen von der schöpferischen Kraft der Zeichenkunst, die damals einen besonderen Höhepunkt erlebte. Faszinierende und doch bislang wenig bekannte Künstler wie Michelangelo Anselmi sind ebenso vertreten wie gefeierte Namen, beispielsweise Andrea Boscoli, Annibale, Agostino und Ludovico Carracci, Giovanni Francesco Barbieri, genannt Guercino, Claude Lorrain, Pier Francesco Mola, Jacopo Palma il Giovane, Giovanni Battista Tiepolo und Taddeo Zuccari. Ihnen und vielen anderen kann man gleichsam über die Schulter schauen, wie sie mit Stift, Feder oder Pinsel die eigenen Ideen – seien es Figuren, Bilderzählungen oder Landschaften – mal flüchtig skizzieren, mal sorgsam durcharbeiten. Wie kaum ein anderes Medium ermöglichen es Zeichnungen, kreatives Schaffen aus allernächster Nähe zu erleben – ein Dialog über Jahrhunderte hinweg. Henning Hoesch, Sammler: „Ich freue mich sehr über die Möglichkeit, eine repräsentative Auswahl meiner in über 40 Jahren zusammengetragenen Sammlung mit der Öffentlichkeit zu teilen. Die Zeichnungen alter Meister geben Einblick in deren Bemühungen und individuelle Fähigkeiten, die Wirklichkeit zu beobachten und festzuhalten — oft naturgetreuer als auf dem gemalten Bild. Im Zentrum steht dabei der Blick auf die Zeichnung als Ursprung aller Kunst und als ein Raum der künstlerischen Auseinandersetzung mit sich selbst. Durch die Unmittelbarkeit des Mediums sind wir eingeladen, diese suchenden Prozesse nachzuvollziehen und zu erkunden. Das Dresdner Kupferstich-Kabinett mit seiner langen Tradition einerseits und der innovativen Arbeit in der Forschung andererseits ist dafür ein idealer Ort.“ Deutlich wird, dass auch Sammeln ein kreativer Prozess ist und die entstehende Sammlung Hoesch kein abgeschlossener Organismus: Stets kommen neue Werke hinzu, andere werden wiederum weitergegeben. Von diesem lebendigen Charakter des Bestands zeugen auch die jüngsten Neuzugänge, darunter eine Interpretation Battista Francos nach einem Idealbildnis von der Hand Michelangelos aus der Gruppe der sogenannten “Teste Divine” (Göttliche Köpfe). Stephanie Buck, Direktorin des Kupferstich-Kabinetts: „In Dresden freuen wir uns außerordentlich, Henning Hoeschs auf dem internationalen Markt über viele Jahre mit Kenntnis und Liebe zusammengetragene Zeichnungssammlung erstmals der Öffentlichkeit zeigen zu können, und zwar im Dialog mit Werken des Kupferstich-Kabinetts. Die vom Blick des privaten Sammlers mitgeprägte Ausstellung ist Ausdruck einer über mehrere Jahre gewachsenen vertrauensvollen Freundschaft, für die ich der Familie Henning Hoesch herzlich danke. Sie fällt in eine Zeit, in der wir im Kupferstich-Kabinett mit einer Gruppe junger Wissenschaftler*innen intensiv zu Renaissance-Zeichnungen forschen und dabei innovative Wege beschreiten. Die Vielfalt der Perspektiven gehört hier wesentlich dazu.“ Am Kupferstich-Kabinett läuft derzeit ein Katalogisierungsprojekt zu den italienischen Zeichnungen des 16. Jahrhunderts, das seit 2018 durch die Getty Foundation im Rahmen der Initiative „The Paper Project. Prints and Drawing Curatorship in the 21th Century“ gefördert wird. Einzelne Blätter aus dieser Bestandsgruppe werden der Präsentation der Sammlung Hoesch zur Seite gestellt und ihr aktueller Forschungsstand besprochen. Ein erster wissenschaftlicher Katalog über die Sammlung Hoesch erschien 2017 im Michael Imhof Verlag unter dem Titel „Galleria Portatile“. Der zweite Band, herausgegeben von Dr. Henning Hoesch und Dr. Heiko Damm, erscheint während der Ausstellungslaufzeit.')
    db.session.add(exhibition)
    db.session.commit()

    # Media types
    audio = MediaType(name="Audio")
    video = MediaType(name="Video")
    image = MediaType(name="Bilder")
    text = MediaType(name="Text")
    object = MediaType(name="3D Objekt")
    
    # Interaction types
    zoom = Interaction(name="Vergrößern")
    compare = Interaction(name="Vergleichen")
    point_and_click = Interaction(name="Zeigen und Klicken")
    touch = Interaction(name="Berühren")
    connect = Interaction(name="Verknüpfen")
    move = Interaction(name="Bewegen")
    focus = Interaction(name="Fokussieren")
    
    # Interactive Visualization realization
    slideshow = Visualization(name="Diashow")
    glyph = Visualization(name="Glyphen")
    timeline = Visualization(name="Zeitstrahl")
    map = Visualization(name="Karte")
    book = Visualization(name="Buch")
    tiles = Visualization(name="Kacheln")
    

    db.session.add_all([audio, video, image, text, object, zoom, compare, point_and_click, touch, connect, move, focus, slideshow, glyph, timeline, map, book, tiles])
    db.session.commit()

    # Create the first media station
    mediastation1 = MediaStation(title="Meisterzeichnungen Hoesch", image_url="", description="Entdecken Sie die faszinierende Welt der Meisterzeichnungen mit unserer interaktiven Medienstation! Auf Tablets und PCs können Sie durch einen benutzerfreundlichen Slider die ausgestellten Werke der Sammlung Hoesch sowie ausgewählte Blätter des Kupferstich-Kabinetts erkunden. Jede Zeichnung wird von informativen Texten begleitet, die Einblicke in die Künstler und deren Schaffensprozess bieten. Tauchen Sie ein in die Kunst der Renaissance und des Barock und erleben Sie hautnah die kreative Kraft der Zeichenkunst. Nutzen Sie die Gelegenheit, Meisterwerke von Michelangelo Anselmi, Andrea Boscoli, Claude Lorrain und vielen anderen aus nächster Nähe zu betrachten.", path_to_exec="test.html", exhibition_id=exhibition.id)
    db.session.add(mediastation1)
    db.session.commit()

    # Create media content for the first media station
    media_content1 = MediaContent(mediastation_id=mediastation1.id)
    media_content1.media_types.extend([text, image])
    media_content1.interactions.extend([touch, point_and_click])
    media_content1.visualizations.extend([slideshow])

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
    station1 = MediaStation.query.filter_by(id=1).first()
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
