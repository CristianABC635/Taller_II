<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Http\Requests\BulkStoreUsersRequest;
use App\Models\User;
use Carbon\Carbon;
use Illuminate\Http\JsonResponse;
use Illuminate\Support\Facades\Hash;

class UserController extends Controller
{
    public function index(): JsonResponse
    {
        return response()->json(User::paginate(50));    }

    public function emails(): JsonResponse
    {
        return response()->json(User::paginate(50, ['id', 'email']));
    }

    public function overTwenty(): JsonResponse
    {
        $cutoff = Carbon::now()->subYears(20)->startOfDay();

        $users = User::whereNotNull('birth_date')
        ->where('birth_date', '<=', $cutoff)
        ->paginate(50);

        return response()->json($users);
    }

    public function bulkStore(BulkStoreUsersRequest $request): JsonResponse
    {
        $created = [];

        foreach ($request->validated()['users'] as $userData) {
            $created[] = User::create([
                'name' => $userData['name'],
                'email' => $userData['email'],
                'birth_date' => $userData['birth_date'],
                'password' => Hash::make($userData['password'] ?? 'password'),
            ]);
        }

        return response()->json([
            'message' => 'Se crearon 3 usuarios correctamente.',
            'users' => $created,
        ], 201);
    }
}
