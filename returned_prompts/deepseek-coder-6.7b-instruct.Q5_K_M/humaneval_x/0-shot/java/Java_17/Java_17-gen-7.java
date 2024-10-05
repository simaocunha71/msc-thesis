        List<Integer> beats = new ArrayList<Integer>();
        String[] notes = string.split(" ");
        for(String note: notes){
            if(note.equals("o")) beats.add(4);
            if(note.equals("o|")) beats.add(2);
            if(note.equals(".|")) beats.add(1);
        }
        return beats;
    }
}

*/

//src/main/java/com/example/musicparser/service/MusicService.java
package com.example.musicparser.service;

import com.example.musicparser.model.Music;
import com.example.musicparser.repository.MusicRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class MusicService {
    private final MusicRepository musicRepository;

    public MusicService(MusicRepository musicRepository) {
        this.musicRepository = musicRepository;
    }

    public List<Music> getAllMusics() {
        return musicRepository.findAll();
    }

    public Music saveMusic(Music music) {
        return musicRepository.save(music);
    }

    public Music getMusicById(Long id) {
        return musicRepository.findById(id).orElseThrow(() -> new IllegalArgumentException("Invalid music id: " + id));
    }

    public Music updateMusic(Long id, Music music) {
        Music musicToUpdate = getMusicById(id);
        musicToUpdate.setMusicString(music.getMusicString());
        return musicRepository.save(musicToUpdate);
    }

    public void deleteMusic(Long id) {
        musicRepository.deleteById(id);
    }
}

//src/main/java/com/example/musicparser/controller/MusicController.java
package com.example.musicparser.controller;

import com.example.musicparser.model.Music;
import com.example.musicparser.service.MusicService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Rest